
# pipeline_tcc.py

# ------------------------------
# 📦 Imports
# ------------------------------
import pandas as pd
import numpy as np
import linecache
import random
from collections import defaultdict
import os
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# ------------------------------
# 0. 📥 Formatação inicial dos dados brutos da PNAD
# ------------------------------
def formatar_dados_pnad_ajustado(
    caminho_dicionario="campos_dicionario.txt",
    caminho_microdados="raw/PNADC_2023_visita1_20241220/PNADC_2023_visita1.txt",
    n_amostras=100000,
    salvar_em="PNAD_2023_formatado.csv"
):
    # Leitura do dicionário
    try:
        dicionario = pd.read_csv(caminho_dicionario, sep="\t", encoding="utf-8")
    except UnicodeDecodeError:
        dicionario = pd.read_csv(caminho_dicionario, sep="\t", encoding="latin1")

    dicionario["Posição Inicial"] = dicionario["Posição Inicial"].astype(int) - 1
    larguras = dicionario["Tamanho"].astype(int).tolist()
    nomes = dicionario["Descrição"].tolist()

    # Corrigir nomes duplicados
    contador = {}
    nomes_corrigidos = []
    for col in nomes:
        if col in contador:
            contador[col] += 1
            nomes_corrigidos.append(f"{col}_{contador[col]}")
        else:
            contador[col] = 1
            nomes_corrigidos.append(col)

    # Contar linhas por UF
    pos_uf = (5, 7)
    contagem_ufs = defaultdict(list)
    with open(caminho_microdados, "r", encoding="latin1") as f:
        for i, linha in enumerate(f):
            uf = linha[pos_uf[0]:pos_uf[1]]
            contagem_ufs[uf].append(i + 1)

    # Amostragem proporcional
    amostragem = []
    amostras_por_uf = n_amostras // len(contagem_ufs)
    for uf, linhas in contagem_ufs.items():
        selecionadas = random.sample(linhas, min(len(linhas), amostras_por_uf))
        amostragem.extend(selecionadas)

    # Gerar DataFrame diretamente
    linhas_texto = [linecache.getline(caminho_microdados, i) for i in amostragem]
    df = pd.read_fwf(pd.io.common.StringIO(''.join(linhas_texto)),
                     widths=larguras, names=nomes_corrigidos, encoding="latin1")

    # Limpeza
    df.drop(columns=df.columns[df.isnull().all()], inplace=True)
    for col in df.select_dtypes(include="float64").columns:
        if df[col].isnull().sum() == 0:
            df[col] = df[col].astype(int)

    # Renomeações
    df.rename(columns={
        'Unidade da Federação': 'UF',
        'Sexo (1 - Masculino, 2 - Feminino)': 'Sexo',
        'Cor ou raça': 'Cor_Raca',
        'Idade do morador na data de referência': 'Idade',
        'Nível de instrução mais elevado que frequentava': 'Escolaridade_Num',
        'Rendimento mensal habitualmente recebido de todos os trabalhos': 'Renda_Habitual',
    }, inplace=True)

    # Mapeamentos
    df['Sexo'] = df['Sexo'].map({1: 'Masculino', 2: 'Feminino'})
    df['Cor_Raca'] = df['Cor_Raca'].map({1: 'Branca', 2: 'Preta', 3: 'Amarela', 4: 'Parda', 5: 'Indígena'})

    # Cálculo de renda total
    colunas_renda = [col for col in df.columns if 'reais' in col.lower()]
    colunas_renda_validas = [col for col in colunas_renda if df[col].dtype in ['float64', 'int64']]
    df['Renda_Total'] = df[colunas_renda_validas].fillna(0).sum(axis=1)

    # Calcular log_renda
    df = df[df['Renda_Total'] > 0].copy()
    df['log_renda'] = df['Renda_Total'].apply(lambda x: np.log1p(x))

    # Salvar resultado final
    df.to_csv(salvar_em, index=False, encoding="utf-8-sig")
    return df

# ------------------------------
# 🔍 Análise Exploratória
# ------------------------------

def analise_exploratoria(df, rais_path='consulta_rais.csv', salvar_em='insumo_dashboard'):
    os.makedirs(salvar_em, exist_ok=True)

    # ------------------------------
    # 1. Integração com RAIS
    # ------------------------------
    rais_df = pd.read_csv(rais_path)
    df = df.merge(rais_df, how='left', on=['sigla_uf', 'sexo', 'grau_instrucao', 'faixa_etaria'])

    # ------------------------------
    # 2. Conversões e colunas auxiliares
    # ------------------------------
    df['Idade'] = pd.to_numeric(df['Idade'], errors='coerce')
    df['Renda_Total'] = pd.to_numeric(df['Renda_Total'], errors='coerce')

    # Faixas etárias
    bins = [0, 17, 25, 35, 45, 55, 65, 80, 150]
    labels = ['0–17', '18–25', '26–35', '36–45', '46–55', '56–65', '66–80', '81+']
    df['Faixa_Etaria'] = pd.cut(df['Idade'], bins=bins, labels=labels, right=False)

    # Renda Zero
    df['Renda_Zero'] = df['Renda_Total'] == 0

    # Mapeamento da escolaridade
    map_escolaridade = {
        2: "Sem instrução", 3: "Fund. 1ª a 4ª série", 4: "Fund. 5ª a 8ª série", 5: "Fundamental completo",
        6: "Médio incompleto", 7: "Médio completo", 8: "Superior incompleto", 9: "Superior completo",
        10: "Mestrado incompleto", 11: "Mestrado completo", 12: "Doutorado incompleto", 13: "Doutorado completo",
        14: "Alfabetização adultos", 15: "Educação infantil"
    }
    df['Escolaridade_Label'] = df['Curso mais elevado frequentado anteriormente'].map(map_escolaridade)

    # ------------------------------
    # 3. Estatísticas e gráficos principais
    # ------------------------------
    def salvar_grafico(plot_func, filename):
        plt.figure(figsize=(10,6))
        plot_func()
        plt.tight_layout()
        plt.savefig(os.path.join(salvar_em, filename))
        plt.close()

    salvar_grafico(lambda: sns.countplot(x='Sexo', data=df), "distribuicao_sexo.png")
    salvar_grafico(lambda: sns.countplot(x='Cor_Raca', data=df, order=df['Cor_Raca'].value_counts().index), "distribuicao_cor_raca.png")
    salvar_grafico(lambda: sns.countplot(x='UF', data=df, order=df['UF'].value_counts().index), "distribuicao_uf.png")
    salvar_grafico(lambda: df.groupby('Escolaridade_Label')['Renda_Total'].mean().sort_values().plot(kind='barh'), "renda_por_escolaridade.png")
    salvar_grafico(lambda: df.groupby('UF')['Renda_Total'].mean().sort_values().plot(kind='bar'), "renda_por_estado.png")

    # ------------------------------
    # 4. Foco em Rondônia
    # ------------------------------
    df_rondonia = df[df['UF'] == 'Rondônia']
    df_rondonia[['Renda_Total']].describe().to_csv(os.path.join(salvar_em, 'estatisticas_rondonia.csv'))

    # ------------------------------
    # 5. Filtragem de renda
    # ------------------------------
    df_renda_valida = df[(df['Renda_Total'] > 0) & (df['Renda_Total'] < 1_000_000)]

    salvar_grafico(lambda: df_renda_valida.groupby('UF')['Renda_Total'].mean().sort_values().plot(kind='bar'), "renda_valida_por_estado.png")
    salvar_grafico(lambda: df_renda_valida.groupby('UF')['Renda_Total'].median().sort_values().plot(kind='bar'), "mediana_renda_estado.png")

    # ------------------------------
    # 6. Histograma no Espírito Santo
    # ------------------------------
    df_es = df_renda_valida[df_renda_valida['UF'] == 'Espírito Santo']
    salvar_grafico(lambda: df_es['Renda_Total'].hist(bins=50), "histograma_es.png")

    # ------------------------------
    # 7. Tabelas para dashboard
    # ------------------------------
    df.to_csv(os.path.join(salvar_em, 'dados_limpos_exploracao.csv'), index=False, encoding='utf-8-sig')
    df_renda_valida.to_csv(os.path.join(salvar_em, 'dados_renda_valida.csv'), index=False, encoding='utf-8-sig')

    return df, df_renda_valida

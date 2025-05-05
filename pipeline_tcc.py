
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

# Novos imports para Machine Learning
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from catboost import CatBoostRegressor
from sklearn.metrics import mean_squared_error, r2_score
import json


# ------------------------------
# 0. 📥 Formatação inicial dos dados brutos da PNAD
# ------------------------------
def formatar_dados_pnad_ajustado(
    caminho_dicionario="data/campos_dicionario.txt",
    caminho_microdados="raw/PNADC_2023_visita1_20241220/PNADC_2023_visita1.txt",
    n_amostras=100000,
    salvar_em="data/PNAD_2023_formatado.csv"
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
        'Curso mais elevado frequentado anteriormente': 'Escolaridade_Num',
        'Rendimento mensal habitualmente recebido de todos os trabalhos': 'Renda_Habitual',
    }, inplace=True)

   # Mapeamentos
    df['Sexo'] = df['Sexo'].map({1: 'Masculino', 2: 'Feminino'})
    df['Cor_Raca'] = df['Cor_Raca'].map({1: 'Branca', 2: 'Preta', 3: 'Amarela', 4: 'Parda', 5: 'Indígena'})

    # Corrigir tipos para o merge com RAIS
    df['sexo'] = df['Sexo'].map({'Masculino': 1, 'Feminino': 2})  # <-- aqui!

    # Cálculo de renda total
    colunas_renda = [col for col in df.columns if 'reais' in col.lower()]
    colunas_renda_validas = [col for col in colunas_renda if df[col].dtype in ['float64', 'int64']]
    df['Renda_Total'] = df[colunas_renda_validas].fillna(0).sum(axis=1)

    # Calcular log_renda
    df = df[df['Renda_Total'] > 0].copy()
    df['log_renda'] = df['Renda_Total'].apply(lambda x: np.log1p(x))

    # Criar colunas auxiliares para merge com a RAIS
    map_uf = {
        11: 'RO', 12: 'AC', 13: 'AM', 14: 'RR', 15: 'PA', 16: 'AP', 17: 'TO',
        21: 'MA', 22: 'PI', 23: 'CE', 24: 'RN', 25: 'PB', 26: 'PE', 27: 'AL',
        28: 'SE', 29: 'BA', 31: 'MG', 32: 'ES', 33: 'RJ', 35: 'SP',
        41: 'PR', 42: 'SC', 43: 'RS', 50: 'MS', 51: 'MT', 52: 'GO', 53: 'DF'
    }
    df['sigla_uf'] = df['UF'].map(map_uf)
    df['grau_instrucao'] = df['Escolaridade_Num']
    df['faixa_etaria'] = pd.cut(
        df['Idade'],
        bins=[0, 17, 25, 35, 45, 55, 65, 80, 150],
        labels=['0–17', '18–25', '26–35', '36–45', '46–55', '56–65', '66–80', '81+'],
        right=False
    )

    # Salvar resultado final
    df.to_csv(salvar_em, index=False, encoding="utf-8-sig")
    return df

# ------------------------------
# 🔍 Análise Exploratória
# ------------------------------

def analise_exploratoria(df, rais_path='data/consulta_rais.csv', salvar_em='insumo_dashboard'):
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
    df['Escolaridade_Label'] = df['grau_instrucao'].map(map_escolaridade)

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

# ------------------------------
# 🤖 Modelagem e Predição
# ------------------------------
def treinar_modelos(df, salvar_em='resultados_ml'):
    os.makedirs(salvar_em, exist_ok=True)

    # Selecionar variáveis
    cat_cols = ['Sexo', 'Cor_Raca', 'UF', 'Escolaridade_Label', 'Faixa_Etaria']
    num_cols = ['Idade', 'Renda_Total']
    target = 'log_renda'

    X = df[cat_cols + num_cols]
    y = df[target]

    # Pré-processamento
    preprocessor = ColumnTransformer([
        ('cat', OneHotEncoder(handle_unknown='ignore'), cat_cols),
        ('num', SimpleImputer(strategy='mean'), num_cols)
    ])

    X_encoded = preprocessor.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

    # Modelos para treino
    modelos = {
        "LinearRegression": LinearRegression(),
        "RandomForest": RandomForestRegressor(random_state=42),
        "GradientBoosting": GradientBoostingRegressor(random_state=42),
        "XGBoost": XGBRegressor(random_state=42, verbosity=0),
        "LightGBM": LGBMRegressor(random_state=42),
        "CatBoost": CatBoostRegressor(verbose=0, random_state=42)
    }

    resultados = {}

    for nome, modelo in modelos.items():
        modelo.fit(X_train, y_train)
        y_pred = modelo.predict(X_test)

        r2 = r2_score(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))

        resultados[nome] = {
            "R2": r2,
            "RMSE": rmse
        }

        # Salvar previsões
        pd.DataFrame({'Real': y_test, 'Predito': y_pred}).to_csv(f"{salvar_em}/predicoes_{nome}.csv", index=False)

        # Salvar gráfico de Real vs Predito
        plt.figure(figsize=(8,6))
        sns.scatterplot(x=y_test, y=y_pred, alpha=0.5)
        plt.xlabel('Real')
        plt.ylabel('Predito')
        plt.title(f'Real vs Predito - {nome}')
        plt.tight_layout()
        plt.savefig(f"{salvar_em}/grafico_real_predito_{nome}.png")
        plt.close()

    # Salvar métricas gerais
    with open(f"{salvar_em}/metricas_modelos.json", "w") as f:
        json.dump(resultados, f, indent=4)

    return resultados

# ------------------------------
# 📊 Criação do Dashboard
# ------------------------------
import streamlit as st

def criar_dashboard():
    st.title("Análise de Renda - PNAD 2023")
    
    # Carregar dados
    df = pd.read_csv('insumo_dashboard/dados_limpos_exploracao.csv')
    df_renda_valida = pd.read_csv('insumo_dashboard/dados_renda_valida.csv')
    
    st.header("📊 Distribuições e Gráficos")
    st.image('insumo_dashboard/distribuicao_sexo.png')
    st.image('insumo_dashboard/distribuicao_cor_raca.png')
    st.image('insumo_dashboard/distribuicao_uf.png')
    st.image('insumo_dashboard/renda_por_escolaridade.png')
    st.image('insumo_dashboard/renda_por_estado.png')
    st.image('insumo_dashboard/renda_valida_por_estado.png')
    st.image('insumo_dashboard/mediana_renda_estado.png')
    st.image('insumo_dashboard/histograma_es.png')

    st.header("📈 Predições dos Modelos")
    metricas = json.load(open('resultados_ml/metricas_modelos.json'))
    for modelo, metrica in metricas.items():
        st.subheader(f"Modelo: {modelo}")
        st.write(metrica)
        st.image(f'resultados_ml/grafico_real_predito_{modelo}.png')

    st.header("🔎 Estatísticas de Rondônia")
    stats_rondonia = pd.read_csv('insumo_dashboard/estatisticas_rondonia.csv')
    st.dataframe(stats_rondonia)

    st.header("🗂️ Filtros Interativos")
    uf_selecionada = st.selectbox("Escolha o Estado (UF):", df['UF'].unique())
    sexo_selecionado = st.selectbox("Escolha o Sexo:", df['Sexo'].unique())
    escolaridade_selecionada = st.selectbox("Escolha a Escolaridade:", df['Escolaridade_Label'].dropna().unique())

    filtro = (df['UF'] == uf_selecionada) & (df['Sexo'] == sexo_selecionado) & (df['Escolaridade_Label'] == escolaridade_selecionada)
    st.dataframe(df[filtro][['UF', 'Sexo', 'Escolaridade_Label', 'Renda_Total']])


if __name__ == '__main__':
    # 1. Formatar dados
    df_formatado = formatar_dados_pnad_ajustado()

    # 2. Análise exploratória
    df_analise, df_renda_valida = analise_exploratoria(df_formatado)

    # 3. Predição
    treinar_modelos(df_renda_valida)

    # 4. Dashboard (manual com comando)
    # Para rodar: streamlit run pipeline_tcc.py
    criar_dashboard()

    # comando para rodar o script
    # streamlit run pipeline_tcc.py
    # ou
    # python pipeline_tcc.py

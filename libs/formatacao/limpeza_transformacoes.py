# libs/formatacao_pnad/limpeza_transformacoes.py

import pandas as pd
import numpy as np

def aplicar_transformacoes(df):
    """
    Realiza as transformações e limpezas no DataFrame da PNAD:
    - renomeações
    - mapeamentos
    - cálculo de renda
    - log(renda)
    - faixa etária
    - colunas auxiliares para merge com RAIS
    """

    # Renomear colunas principais
    df.rename(columns={
        'Unidade da Federação': 'UF',
        'Sexo (1 - Masculino, 2 - Feminino)': 'Sexo',
        'Cor ou raça': 'Cor_Raca',
        'Idade do morador na data de referência': 'Idade',
        'Curso mais elevado frequentado anteriormente': 'Escolaridade_Num',
        'Rendimento mensal habitualmente recebido de todos os trabalhos': 'Renda_Habitual',
    }, inplace=True)

    # Mapear sexo e cor
    df['Sexo'] = df['Sexo'].map({1: 'Masculino', 2: 'Feminino'})
    df['Cor_Raca'] = df['Cor_Raca'].map({
        1: 'Branca', 2: 'Preta', 3: 'Amarela', 4: 'Parda', 5: 'Indígena'
    })

    # Coluna auxiliar para merge com RAIS
    df['sexo'] = df['Sexo'].map({'Masculino': 1, 'Feminino': 2})

    # Cálculo da Renda Total
    colunas_renda = [col for col in df.columns if 'reais' in col.lower()]
    colunas_validas = [col for col in colunas_renda if df[col].dtype in ['float64', 'int64']]
    df['Renda_Total'] = df[colunas_validas].fillna(0).sum(axis=1)

    # Filtrar apenas quem tem renda positiva
    df = df[df['Renda_Total'] > 0].copy()

    # Calcular log_renda
    df['log_renda'] = df['Renda_Total'].apply(lambda x: np.log1p(x))

    # Criar colunas auxiliares para merge
    map_uf = {
        11: 'RO', 12: 'AC', 13: 'AM', 14: 'RR', 15: 'PA', 16: 'AP', 17: 'TO',
        21: 'MA', 22: 'PI', 23: 'CE', 24: 'RN', 25: 'PB', 26: 'PE', 27: 'AL',
        28: 'SE', 29: 'BA', 31: 'MG', 32: 'ES', 33: 'RJ', 35: 'SP',
        41: 'PR', 42: 'SC', 43: 'RS', 50: 'MS', 51: 'MT', 52: 'GO', 53: 'DF'
    }
    df['sigla_uf'] = df['UF'].map(map_uf)
    df['grau_instrucao'] = df['Escolaridade_Num']

    # Faixa etária
    df['faixa_etaria'] = pd.cut(
        df['Idade'],
        bins=[0, 17, 25, 35, 45, 55, 65, 80, 150],
        labels=['0–17', '18–25', '26–35', '36–45', '46–55', '56–65', '66–80', '81+'],
        right=False
    )

    return df
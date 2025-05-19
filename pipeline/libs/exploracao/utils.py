# libs/exploracao/utils.py

import pandas as pd
import numpy as np

# 🎓 Mapeamento de escolaridade
MAP_ESCOLARIDADE = {
    2: "Sem instrução", 3: "Fund. 1ª a 4ª série", 4: "Fund. 5ª a 8ª série", 5: "Fundamental completo",
    6: "Médio incompleto", 7: "Médio completo", 8: "Superior incompleto", 9: "Superior completo",
    10: "Mestrado incompleto", 11: "Mestrado completo", 12: "Doutorado incompleto", 13: "Doutorado completo",
    14: "Alfabetização adultos", 15: "Educação infantil"
}

# 🧮 Faixas etárias padronizadas
FAIXAS_ETARIAS = pd.IntervalIndex.from_tuples([
    (0, 17), (17, 25), (25, 35), (35, 45), (45, 55), (55, 65), (65, 80), (80, 150)
], closed='left')
LABELS_FAIXAS = ['0–17', '18–25', '26–35', '36–45', '46–55', '56–65', '66–80', '81+']

def preparar_dados_exploracao(df: pd.DataFrame, rais_path: str) -> pd.DataFrame:
    """Realiza as transformações iniciais, cria colunas auxiliares e integra RAIS."""

    # Integração RAIS
    rais_df = pd.read_csv(rais_path)
    df = df.merge(rais_df, how='left', on=['sigla_uf', 'sexo', 'grau_instrucao', 'faixa_etaria'])

    # Conversão de colunas
    df['Idade'] = pd.to_numeric(df['Idade'], errors='coerce')
    df['Renda_Total'] = pd.to_numeric(df['Renda_Total'], errors='coerce')

    # Faixa etária
    df['Faixa_Etaria'] = pd.cut(df['Idade'], bins=FAIXAS_ETARIAS, labels=LABELS_FAIXAS, right=False)

    # Escolaridade categórica
    df['Escolaridade_Label'] = df['grau_instrucao'].map(MAP_ESCOLARIDADE)

    # Renda zero
    df['Renda_Zero'] = df['Renda_Total'] == 0

    return df

def filtrar_renda_valida(df: pd.DataFrame) -> pd.DataFrame:
    """Remove valores extremos ou inválidos da renda total."""
    return df[(df['Renda_Total'] > 0) & (df['Renda_Total'] < 1_000_000)]

def gerar_estatisticas_rondonia(df: pd.DataFrame) -> pd.DataFrame:
    """Extrai estatísticas descritivas da renda em Rondônia."""
    df_ro = df[df['UF'] == 'Rondônia']
    return df_ro[['Renda_Total']].describe().round(2)
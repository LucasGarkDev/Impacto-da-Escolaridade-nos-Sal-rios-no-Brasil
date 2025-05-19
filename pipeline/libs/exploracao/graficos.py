# libs/exploracao/graficos.py

import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def salvar_grafico(plot_func, caminho_arquivo: str, figsize=(10, 6)):
    """Gera e salva um gráfico com função customizada."""
    plt.figure(figsize=figsize)
    plot_func()
    plt.tight_layout()
    plt.savefig(caminho_arquivo)
    plt.close()

def gerar_graficos_distribuicoes(df: pd.DataFrame, destino: str):
    """Gera gráficos de distribuição demográfica e escolaridade."""
    os.makedirs(destino, exist_ok=True)

    salvar_grafico(lambda: sns.countplot(x='Sexo', data=df),
                   os.path.join(destino, "distribuicao_sexo.png"))

    salvar_grafico(lambda: sns.countplot(x='Cor_Raca', data=df, order=df['Cor_Raca'].value_counts().index),
                   os.path.join(destino, "distribuicao_cor_raca.png"))

    salvar_grafico(lambda: sns.countplot(x='UF', data=df, order=df['UF'].value_counts().index),
                   os.path.join(destino, "distribuicao_uf.png"))

    salvar_grafico(lambda: df.groupby('Escolaridade_Label')['Renda_Total'].mean().sort_values().plot(kind='barh'),
                   os.path.join(destino, "renda_por_escolaridade.png"))

    salvar_grafico(lambda: df.groupby('UF')['Renda_Total'].mean().sort_values().plot(kind='bar'),
                   os.path.join(destino, "renda_por_estado.png"))

def gerar_graficos_renda_filtrada(df_filtrado: pd.DataFrame, destino: str):
    """Gera gráficos com base nos dados de renda validada."""
    salvar_grafico(lambda: df_filtrado.groupby('UF')['Renda_Total'].mean().sort_values().plot(kind='bar'),
                   os.path.join(destino, "renda_valida_por_estado.png"))

    salvar_grafico(lambda: df_filtrado.groupby('UF')['Renda_Total'].median().sort_values().plot(kind='bar'),
                   os.path.join(destino, "mediana_renda_estado.png"))

def gerar_histograma_estado(df_filtrado: pd.DataFrame, estado: str, destino: str):
    """Gera histograma da renda para um estado específico."""
    df_estado = df_filtrado[df_filtrado['UF'] == estado]
    salvar_grafico(lambda: df_estado['Renda_Total'].hist(bins=50),
                   os.path.join(destino, f"histograma_{estado.lower().replace(' ', '_')}.png"))
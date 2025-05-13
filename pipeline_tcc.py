

# ------------------------------
# 📦 Imports
# ------------------------------
import os
import json
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 📚 Módulos internos
from libs.formatacao import formatar_dados_pnad
from libs.exploracao import analise_exploratoria
from gerar_relatorio import gerar_relatorio_html

# 🤖 Machine Learning
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from catboost import CatBoostRegressor
from sklearn.metrics import mean_squared_error, r2_score

# 📊 Streamlit Dashboard
import streamlit as st



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


# ------------------------------
# Execução do Pipeline
# ------------------------------
if __name__ == '__main__':
    # 1. Formatar dados
    df_formatado = formatar_dados_pnad()
    print("✅ Dados formatados com sucesso!")

    # 2. Análise exploratória
    df_analise, df_renda_valida = analise_exploratoria(df_formatado)
    print("✅ Análise exploratória realizada com sucesso!")

    # 3. Predição
    treinar_modelos(df_renda_valida)
    print("✅ Modelos treinados com sucesso!")

    # 4. Geração de relatório
    gerar_relatorio_html()
    print("✅ Relatório gerado com sucesso!")

    # 5. Dashboard (manual com comando)
    criar_dashboard()
    print("✅ Dashboard criado com sucesso!")

    



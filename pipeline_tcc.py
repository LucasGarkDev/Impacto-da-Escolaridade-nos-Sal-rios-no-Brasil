

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

    



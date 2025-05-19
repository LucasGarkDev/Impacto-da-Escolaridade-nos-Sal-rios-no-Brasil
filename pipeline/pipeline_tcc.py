# pipeline_tcc.py

# ------------------------------
# 📦 Imports
# ------------------------------
import os
import pandas as pd
import json

# 📚 Módulos internos
from libs.formatacao import formatar_dados_pnad
from libs.exploracao import analise_exploratoria
from libs.modelagem import treinar_modelos
from gerar_relatorio import gerar_relatorio_html

# 📊 Streamlit Dashboard
# from dashboard import criar_dashboard

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
# 🚀 Execução do Pipeline
# ------------------------------
if __name__ == '__main__':
    # 1. Formatar os dados brutos
    df_formatado = formatar_dados_pnad()
    print("✅ Dados formatados com sucesso!")

    # 2. Realizar análise exploratória e gerar gráficos
    df_analise, df_renda_valida = analise_exploratoria(df_formatado)
    print("✅ Análise exploratória realizada com sucesso!")

    # 3. Treinar modelos e salvar métricas e predições
    treinar_modelos(df_renda_valida)
    print("✅ Modelos treinados com sucesso!")

    # 4. Gerar relatório HTML/PDF
    gerar_relatorio_html()
    print("✅ Relatório gerado com sucesso!")

    # 5. Criar dashboard interativo com Streamlit
    criar_dashboard()
    print("✅ Dashboard criado com sucesso!")

    



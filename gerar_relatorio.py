# gerar_relatorio.py

import os
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import json
import pandas as pd

def gerar_relatorio_html():
    # Caminhos
    template_dir = "templates"
    output_dir = "relatorio_final"
    os.makedirs(output_dir, exist_ok=True)

    # Carregar métricas
    with open("resultados_ml/metricas_modelos.json", "r") as f:
        metricas = json.load(f)

    # Transformar o dicionário de métricas em DataFrame
    df_metricas = pd.DataFrame(metricas).T.reset_index()
    df_metricas.columns = ['Modelo', 'R²', 'RMSE']
    tabela_metricas = df_metricas.round(4).to_html(index=False, classes='tabela')

    # Estatísticas de Rondônia
    stats_rondonia = pd.read_csv("insumo_dashboard/estatisticas_rondonia.csv").round(2).to_html(index=False)

    # Gráficos a serem incluídos
    graficos = [
        "distribuicao_sexo.png",
        "distribuicao_cor_raca.png",
        "distribuicao_uf.png",
        "renda_por_escolaridade.png",
        "renda_por_estado.png",
        "renda_valida_por_estado.png",
        "mediana_renda_estado.png",
        "histograma_es.png",
    ]
    graficos_modelos = [f"grafico_real_predito_{modelo}.png" for modelo in metricas.keys()]

    # Renderizar HTML
   # Estatísticas de Rondônia
    stats_rondonia = pd.read_csv("insumo_dashboard/estatisticas_rondonia.csv").round(2).to_html(index=False)
    tabela_estatisticas = stats_rondonia  # <-- ESSA LINHA ESTAVA FALTANDO

    # Renderizar HTML
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template("template_relatorio.html")
    html_content = template.render(
        metricas=metricas,
        graficos=graficos,
        graficos_modelos=graficos_modelos,
        stats_rondonia=stats_rondonia,
        tabela_metricas=tabela_metricas,
        tabela_estatisticas=tabela_estatisticas  # agora está definida
    )

    tabela_estatisticas = pd.read_csv("insumo_dashboard/estatisticas_rondonia.csv").round(2).to_html(index=False)

    # Salvar HTML
    html_path = os.path.join(output_dir, "relatorio.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    # Converter para PDF
    HTML(html_path).write_pdf(os.path.join(output_dir, "relatorio.pdf"))
    print("✅ Relatório gerado com sucesso!")
    print("📊 Métricas carregadas:", metricas)
    print("📋 Estatísticas de Rondônia (head):")
    print(stats_rondonia)
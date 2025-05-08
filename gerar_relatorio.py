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
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template("template_relatorio.html")
    html_content = template.render(
        metricas=metricas,
        graficos=graficos,
        graficos_modelos=graficos_modelos,
        stats_rondonia=stats_rondonia
    )

    # Salvar HTML
    html_path = os.path.join(output_dir, "relatorio.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    # Converter para PDF
    HTML(html_path).write_pdf(os.path.join(output_dir, "relatorio.pdf"))
    print("✅ Relatório gerado com sucesso!")
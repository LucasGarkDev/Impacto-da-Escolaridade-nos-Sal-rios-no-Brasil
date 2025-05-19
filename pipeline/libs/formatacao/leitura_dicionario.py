# libs/formatacao_pnad/leitura_dicionario.py

import pandas as pd

def carregar_dicionario(caminho_dicionario):
    """Carrega e trata o dicionário de dados da PNAD."""
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

    return larguras, nomes_corrigidos

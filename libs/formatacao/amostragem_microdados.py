# libs/formatacao_pnad/amostragem_microdados.py

import random
from collections import defaultdict
import linecache

def amostrar_microdados(caminho_microdados, n_amostras):
    """Realiza amostragem proporcional por UF a partir dos microdados fixos."""
    pos_uf = (5, 7)
    contagem_ufs = defaultdict(list)

    with open(caminho_microdados, "r", encoding="latin1") as f:
        for i, linha in enumerate(f):
            uf = linha[pos_uf[0]:pos_uf[1]]
            contagem_ufs[uf].append(i + 1)

    amostragem = []
    amostras_por_uf = n_amostras // len(contagem_ufs)

    for uf, linhas in contagem_ufs.items():
        selecionadas = random.sample(linhas, min(len(linhas), amostras_por_uf))
        amostragem.extend(selecionadas)

    # Carregar as linhas amostradas
    linhas_texto = [linecache.getline(caminho_microdados, i) for i in amostragem]
    return ''.join(linhas_texto)

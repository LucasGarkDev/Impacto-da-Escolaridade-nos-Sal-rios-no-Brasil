from .leitura_dicionario import ler_dicionario_campos
from .amostragem_microdados import amostrar_microdados
from .leitura_estrutura import ler_microdados
from .limpeza_transformacoes import limpar_e_transformar_dados

def formatar_dados_pnad(
    caminho_dicionario="data/campos_dicionario.txt",
    caminho_microdados="raw/PNADC_2023_visita1_20241220/PNADC_2023_visita1.txt",
    n_amostras=20000,
    salvar_em="data/PNAD_2023_formatado.csv"
):
    # 1. Lê o dicionário de campos
    nomes_corrigidos, larguras = ler_dicionario_campos(caminho_dicionario)

    # 2. Define amostragem proporcional
    linhas_amostradas = amostrar_microdados(caminho_microdados, n_amostras)

    # 3. Lê os dados com base nas amostras
    df = ler_microdados(caminho_microdados, linhas_amostradas, nomes_corrigidos, larguras)

    # 4. Limpeza e transformação
    df_limpo = limpar_e_transformar_dados(df)

    # 5. Salva o resultado
    df_limpo.to_csv(salvar_em, index=False, encoding="utf-8-sig")

    return df_limpo
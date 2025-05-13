# libs/exploracao/exploracao.py

import os
import pandas as pd
from .utils import (
    integrar_com_rais,
    adicionar_variaveis_auxiliares,
    mapear_escolaridade,
    salvar_estatisticas_rondonia
)
from .graficos import (
    gerar_graficos_distribuicoes,
    gerar_graficos_renda_filtrada,
    gerar_histograma_estado
)

def analise_exploratoria(df: pd.DataFrame, rais_path='data/consulta_rais.csv', salvar_em='insumo_dashboard'):
    os.makedirs(salvar_em, exist_ok=True)

    # 1. Integração com RAIS
    df = integrar_com_rais(df, rais_path)

    # 2. Adição de variáveis auxiliares
    df = adicionar_variaveis_auxiliares(df)

    # 3. Mapeamento de escolaridade
    df = mapear_escolaridade(df)

    # 4. Estatísticas para Rondônia
    salvar_estatisticas_rondonia(df, salvar_em)

    # 5. Geração de gráficos principais
    gerar_graficos_distribuicoes(df, salvar_em)

    # 6. Filtro de renda válida
    df_filtrado = df[(df['Renda_Total'] > 0) & (df['Renda_Total'] < 1_000_000)]

    # 7. Gráficos com dados filtrados
    gerar_graficos_renda_filtrada(df_filtrado, salvar_em)
    gerar_histograma_estado(df_filtrado, estado='Espírito Santo', destino=salvar_em)

    # 8. Salvar dados tratados
    df.to_csv(os.path.join(salvar_em, 'dados_limpos_exploracao.csv'), index=False, encoding='utf-8-sig')
    df_filtrado.to_csv(os.path.join(salvar_em, 'dados_renda_valida.csv'), index=False, encoding='utf-8-sig')

    return df, df_filtrado
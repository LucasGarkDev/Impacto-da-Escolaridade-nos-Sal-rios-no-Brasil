import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np
import pandas as pd

def analisar_residuos(y_test, y_pred, nome_modelo, salvar_em='resultados_ml'):
    os.makedirs(salvar_em, exist_ok=True)
    
    residuos = y_test - y_pred

    # Gráfico de resíduos
    plt.figure(figsize=(8, 6))
    sns.histplot(residuos, bins=50, kde=True)
    plt.title(f'Distribuição dos Resíduos - {nome_modelo}')
    plt.xlabel('Resíduos')
    plt.ylabel('Frequência')
    plt.tight_layout()
    plt.savefig(f"{salvar_em}/residuos_{nome_modelo}.png")
    plt.close()

    # Gráfico Real vs Resíduo
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=y_test, y=residuos, alpha=0.5)
    plt.axhline(0, color='red', linestyle='--')
    plt.title(f'Real vs Resíduo - {nome_modelo}')
    plt.xlabel('Valor Real')
    plt.ylabel('Resíduo')
    plt.tight_layout()
    plt.savefig(f"{salvar_em}/real_vs_residuo_{nome_modelo}.png")
    plt.close()

    # Retorno dos resíduos como DataFrame (opcional para debugging)
    return pd.DataFrame({'y_real': y_test, 'residuo': residuos})
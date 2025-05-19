import os
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def exportar_resultados_modelo(nome_modelo, y_test, y_pred, salvar_em='resultados_ml'):
    os.makedirs(salvar_em, exist_ok=True)

    # Métricas
    from sklearn.metrics import r2_score, mean_squared_error
    r2 = r2_score(y_test, y_pred)
    rmse = mean_squared_error(y_test, y_pred, squared=False)

    metricas = {'R2': r2, 'RMSE': rmse}
    with open(f"{salvar_em}/metricas_{nome_modelo}.json", "w") as f:
        json.dump(metricas, f, indent=4)

    # Previsões
    pd.DataFrame({'Real': y_test, 'Predito': y_pred}).to_csv(
        f"{salvar_em}/predicoes_{nome_modelo}.csv", index=False
    )

    # Gráfico
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=y_test, y=y_pred, alpha=0.5)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
    plt.title(f'Real vs Predito - {nome_modelo}')
    plt.xlabel('Real')
    plt.ylabel('Predito')
    plt.tight_layout()
    plt.savefig(f"{salvar_em}/grafico_real_predito_{nome_modelo}.png")
    plt.close()

    return metricas
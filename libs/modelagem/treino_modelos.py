import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import json

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

def treinar_modelos_basicos(X, y, salvar_em='resultados_ml'):
    os.makedirs(salvar_em, exist_ok=True)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    modelos = {
        "LinearRegression": LinearRegression(),
        "RandomForest": RandomForestRegressor(n_estimators=100, random_state=42),
    }

    resultados = {}

    for nome, modelo in modelos.items():
        modelo.fit(X_train, y_train)
        y_pred = modelo.predict(X_test)

        r2 = r2_score(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))

        resultados[nome] = {"R2": r2, "RMSE": rmse}

        pd.DataFrame({
            'Real': y_test,
            'Predito': y_pred
        }).to_csv(f"{salvar_em}/predicoes_{nome}.csv", index=False)

        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=y_test, y=y_pred, alpha=0.5)
        plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
        plt.title(f'Real vs Predito - {nome}')
        plt.xlabel('Real')
        plt.ylabel('Predito')
        plt.tight_layout()
        plt.savefig(f"{salvar_em}/grafico_real_predito_{nome}.png")
        plt.close()

    with open(f"{salvar_em}/metricas_modelos.json", "w") as f:
        json.dump(resultados, f, indent=4)

    return resultados

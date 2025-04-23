
# pipeline_tcc.py

# ------------------------------
# 📦 Imports
# ------------------------------
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from catboost import CatBoostRegressor
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ------------------------------
# 1. 📥 Carregamento dos dados
# ------------------------------
def carregar_dados(caminho_csv):
    df = pd.read_csv(caminho_csv)
    return df

# ------------------------------
# 2. 🧹 Limpeza e tratamento
# ------------------------------
def tratar_dados(df):
    df = df.copy()
    df['Escolaridade_Idade'] = df['Escolaridade_Num'] * df['Idade']
    return df

# ------------------------------
# 3. 🔁 Pré-processamento
# ------------------------------
def preparar_dados(df, cat_cols, num_cols):
    preprocessor = ColumnTransformer(transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), cat_cols),
        ('num', SimpleImputer(strategy='mean'), num_cols)
    ])
    X = df[cat_cols + num_cols]
    y = df['log_renda']
    X_encoded = preprocessor.fit_transform(X)
    feature_names = preprocessor.get_feature_names_out()
    return X_encoded, y, feature_names

# ------------------------------
# 4. 🤖 Treinamento e avaliação
# ------------------------------
def treinar_modelo(X, y, feature_names, salvar_em='resultados_ml'):
    os.makedirs(salvar_em, exist_ok=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    modelo = CatBoostRegressor(verbose=0, random_state=42)
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)
    
    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    # Exportar métricas
    with open(f"{salvar_em}/metricas_modelo.txt", "w") as f:
        f.write(f"R2: {r2}\nRMSE: {rmse}\n")

    # Exportar previsões
    pd.DataFrame({'Real': y_test, 'Previsto': y_pred}).to_csv(f"{salvar_em}/predicoes.csv", index=False)

    # Exportar importância
    importancias = pd.Series(modelo.get_feature_importance(), index=feature_names)
    importancias.sort_values(ascending=False).to_csv(f"{salvar_em}/importancia_variaveis.csv")

    return modelo

# ------------------------------
# 5. 📊 Geração de gráfico
# ------------------------------
def plotar_importancia(modelo, feature_names, salvar_em='resultados_ml'):
    importancias = pd.Series(modelo.get_feature_importance(), index=feature_names)
    plt.figure(figsize=(8,6))
    importancias.sort_values(ascending=True).tail(15).plot(kind='barh')
    plt.title("Importância das Variáveis - CatBoost")
    plt.tight_layout()
    plt.savefig(f"{salvar_em}/grafico_importancia.png")

# ------------------------------
# 🚀 Execução principal
# ------------------------------
if __name__ == '__main__':
    caminho_csv = 'dados_modelagem.csv'  # arquivo de entrada já tratado
    cat_cols = ['Sexo', 'Cor_Raca', 'UF', 'Setor_Economico', 'Area_Atuacao', 'Faixa_Etaria']
    num_cols = ['Idade', 'Escolaridade_Num', 'Escolaridade_Idade']

    df = carregar_dados(caminho_csv)
    df = tratar_dados(df)
    X, y, feature_names = preparar_dados(df, cat_cols, num_cols)
    modelo = treinar_modelo(X, y, feature_names)
    plotar_importancia(modelo, feature_names)

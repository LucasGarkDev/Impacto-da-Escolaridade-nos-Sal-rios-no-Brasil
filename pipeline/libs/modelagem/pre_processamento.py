import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer

def preparar_dados(df, cat_cols, num_cols, target='log_renda'):
    X = df[cat_cols + num_cols]
    y = df[target]

    preprocessor = ColumnTransformer([
        ('cat', OneHotEncoder(handle_unknown='ignore', drop='first'), cat_cols),
        ('num', SimpleImputer(strategy='mean'), num_cols)
    ])

    X_encoded = preprocessor.fit_transform(X)
    return X_encoded, y, preprocessor
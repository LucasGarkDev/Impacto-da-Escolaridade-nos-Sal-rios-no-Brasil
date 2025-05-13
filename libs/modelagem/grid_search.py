from catboost import CatBoostRegressor
from sklearn.model_selection import GridSearchCV

def otimizar_modelo_catboost(X_train, y_train, scoring='neg_root_mean_squared_error'):
    parametros = {
        'depth': [4, 6, 8],
        'learning_rate': [0.01, 0.05, 0.1],
        'iterations': [100, 300]
    }

    modelo = CatBoostRegressor(verbose=0, random_state=42)

    grid = GridSearchCV(
        modelo,
        parametros,
        scoring=scoring,
        cv=3,
        n_jobs=-1
    )

    grid.fit(X_train, y_train)
    return grid.best_estimator_, grid.best_params_, grid.best_score_
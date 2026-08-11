import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from load_data import carregar_dados

def avaliar_modelo():
    df = carregar_dados("data/cars.csv")

    X = df[['ano', 'km', 'potencia']]
    y = df['preco']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )

    modelo = LinearRegression()
    modelo.fit(X_train, y_train)

    previsoes = modelo.predict(X_test)

    mae = mean_absolute_error(y_test, previsoes)
    rmse = np.sqrt(mean_squared_error(y_test, previsoes))
    r2 = r2_score(y_test, previsoes)

    print("--- Avaliação do Modelo nos Dados de Teste ---")
    print(f"MAE (Erro Médio Absoluto): R$ {mae:.2f}")
    print(f"RMSE (Raiz do Erro Quadrático): R$ {rmse:.2f}")
    print(f"R² Score: {r2:.4f}\n")

    comparativo = pd.DataFrame({
        'Valor Real':y_test.values,
        'Previsão':previsoes,
        'Diferença':y_test.values - previsoes
    })

if __name__ == "__main__":
    avaliar_modelo()
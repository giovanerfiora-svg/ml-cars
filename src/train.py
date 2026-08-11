import pandas as pd
from sklearn.linear_model import LinearRegression
from load_data import carregar_dados

def treinar_modelo():
    df = carregar_dados("data/cars.csv")

    X = df[['ano', 'km', 'potencia']]
    y = df['preco']

    modelo = LinearRegression()

    modelo.fit(X, y)

    print("Modelo treinado com sucesso!\n")

    for feature, coef in zip(X.columns, modelo.coef_):
        print(f"Peso para '{feature}': {coef:.2f}")
    print(f"Intercepto (constante): {modelo.intercept_:.2f}")

if __name__ == "__main__":
    treinar_modelo()    
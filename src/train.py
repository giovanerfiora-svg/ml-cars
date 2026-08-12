import os
import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from load_data import carregar_dados

def treinar_e_salvar_modelo():
    diretorio_script = os.path.dirname(os.path.abspath(__file__))
    raiz_projeto = os.path.dirname(diretorio_script)
    
    caminho_csv = os.path.join(raiz_projeto, "data", "cars.csv")
    pasta_models = os.path.join(raiz_projeto, "models")
    caminho_modelo = os.path.join(pasta_models, "modelo_carros.joblib")

    df = carregar_dados(caminho_csv)
    X = df[['ano', 'km', 'potencia']]
    y = df['preco']

    modelo = LinearRegression()
    modelo.fit(X, y)

    print("Modelo treinado com sucesso!\n")
    for feature, coef in zip(X.columns, modelo.coef_):
        print(f"Peso para '{feature}': {coef:.2f}")
    print(f"Intercepto (constante): {modelo.intercept_:.2f}\n")

    os.makedirs(pasta_models, exist_ok=True)
    joblib.dump(modelo, caminho_modelo)
    print(f"[Sucesso] Modelo salvo em: '{caminho_modelo}'\n")

    return modelo

if __name__ == "__main__":
    treinar_e_salvar_modelo()
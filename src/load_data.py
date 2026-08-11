import pandas as pd

def carregar_dados(caminho_csv):
    df = pd.read_csv(caminho_csv)
    return df

if __name__ == "__main__":
    caminho = "data/cars.csv"
    dados = carregar_dados(caminho)

    print("--- Primeiras linhas do dataset ---")
    print(dados.head())

    print("\n--- Informações sobre as colunas ---")
    print(dados.info())

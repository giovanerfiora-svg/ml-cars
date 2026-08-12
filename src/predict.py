import pandas as pd
from sklearn.linear_model import LinearRegression
from load_data import carregar_dados

def treinar_modelo_completo():
    df = carregar_dados("data/cars.csv")
    X = df[['ano', 'km', 'potencia']]
    y = df['preco']

    modelo = LinearRegression()
    modelo.fit(X, y)
    return modelo

def interface_previsao():
    print("========================================")
    print("   ESTIMADOR DE PREÇO DE CARROS (ML)   ")
    print("========================================")

    modelo = treinar_modelo_completo()

    try:
        ano = int(input("Digite o ano do carro (ex: 2018): "))
        km = int(input("Digite a quilometragem (ex: 85000): "))
        potencia = float(input("Digite a potência do motor (ex: 1.6): "))

        novo_carro = pd.DataFrame([{
            'ano':ano,
            'km':km,
            'potencia':potencia
        }])

        preco_estimado = modelo.predict(novo_carro)[0]

        print("\n----------------------------------------")
        print(f"Preço estimado pelo modelo: R$ {preco_estimado:,.2f}")
        print("----------------------------------------\n")

    except ValueError:
        print("\n[Erro] Por favor, insira valores numéricos válidos!")

if __name__ == "__main__":
    interface_previsao()
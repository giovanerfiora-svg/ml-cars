import os
import joblib
from train import treinar_e_salvar_modelo

def carregar_modelo_salvo():
    diretorio_script = os.path.dirname(os.path.abspath(__file__))
    raiz_projeto = os.path.dirname(diretorio_script)
    caminho_modelo = os.path.join(raiz_projeto, "models", "modelo_carros.joblib")

    if not os.path.exists(caminho_modelo):
        print("Arquivo de modelo não encontrado. Iniciando treinamento...")
        return treinar_e_salvar_modelo()

    modelo = joblib.load(caminho_modelo)
    return modelo

def fazer_previsao():
    modelo = carregar_modelo_salvo()

    print("========================================")
    print("      ESTIMADOR DE PREÇO DE CARROS      ")
    print("========================================")

    try:
        ano = int(input("Ano do carro (ex: 2018): "))
        km = float(input("Quilometragem (ex: 45000): "))
        potencia = float(input("Potência do motor (ex: 1.6): "))

        dados_novos = [[ano, km, potencia]]
        preco_estimado = modelo.predict(dados_novos)[0]

        print("\n----------------------------------------")
        print(f"Preço estimado de venda: R$ {preco_estimado:,.2f}")
        print("----------------------------------------\n")

    except ValueError:
        print("\n[Erro] Entrada inválida! Digite apenas números nos campos.")

if __name__ == "__main__":
    fazer_previsao()
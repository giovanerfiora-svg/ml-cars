import os
import joblib
import pandas as pd
from src.load_data import carregar_dados

def test_carregamento_dados():
    raiz_projeto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    caminho_csv = os.path.join(raiz_projeto, "data", "cars.csv")
    
    assert os.path.exists(caminho_csv), "O arquivo cars.csv não foi encontrado na pasta data/"
    
    df = carregar_dados(caminho_csv)
    
    assert not df.empty, "O dataset não pode estar vazio"
    assert list(df.columns) == ['ano', 'km', 'potencia', 'preco'], "As colunas do dataset diferem do esperado"

def test_predicao_modelo():
    raiz_projeto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    caminho_modelo = os.path.join(raiz_projeto, "models", "modelo_carros.joblib")
    
    assert os.path.exists(caminho_modelo), "O arquivo modelo_carros.joblib precisa existir na pasta models/"
    
    modelo = joblib.load(caminho_modelo)
    
    dados_teste = [[2020, 30000, 1.6]]
    preco_estimado = modelo.predict(dados_teste)[0]
    
    assert preco_estimado > 0, "O preço estimado pelo modelo deve ser positivo"
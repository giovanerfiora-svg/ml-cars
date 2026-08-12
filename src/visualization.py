import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from load_data import carregar_dados

def gerar_graficos_analise():

    df = carregar_dados("data/cars.csv")
    X = df[['ano', 'km', 'potencia']]
    y = df['preco']
    
    modelo = LinearRegression()
    modelo.fit(X, y)

    previsoes = modelo.predict(X)
    residuos = y - previsoes

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    ax1.scatter(y, previsoes, color='blue', alpha=0.7, edgecolors='k')

    ax1.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2, label='Previsão Perfeita')
    ax1.set_title('Preço Real vs. Preço Previsto')
    ax1.set_xlabel('Preço Real (R$)')
    ax1.set_ylabel('Preço Previsto (R$)')
    ax1.legend()
    ax1.grid(True)

    ax2.hist(residuos, bins=8, color='orange', edgecolor='black', alpha=0.7)
    ax2.axvline(0, color='red', linestyle='--', linewidth=2, label='Erro Zero')
    ax2.set_title('Distribuição dos Erros (Resíduos)')
    ax2.set_xlabel('Erro em R$ (Real - Previsto)')
    ax2.set_ylabel('Frequência de Carros')
    ax2.legend()
    ax2.grid(True)

    plt.tight_layout()

    print("Exibindo os gráficos...")
    plt.show()

if __name__ == '__main__':
    gerar_graficos_analise()
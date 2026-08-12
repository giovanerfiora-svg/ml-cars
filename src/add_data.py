import csv
import pandas as pd
from train import treinar_modelo

def adicionar_novo_carro(ano, km, potencia, preco_real, caminho_csv="data/cars.csv"):
    nova_linha = [ano, km, potencia, preco_real]

    with open(caminho_csv, mode='a', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(nova_linha)

        print(f"\n[Sucesso] Novo registro adicionado ao arquivo '{caminho_csv}!")

def menu_interativo():
    print("========================================")
    print("   SISTEMA DE GESTÃO E RETREINAMENTO   ")
    print("========================================")
    print("1. Adicionar novo dado real ao dataset")
    print("2. Sair")

    opcao = input("\nEscolha uma opção (1 ou 2): ")

    if opcao == '1':
        try:
            ano = int(input("Ano: "))
            km = int(input("Quilometragem: "))
            potencia = float(input("Potência do motor: "))
            preco_real = float(input("Preço real de venda (R$): "))
        except ValueError:
            print("\n[Erro] Você inseriu um texto onde deveria ser número. Operação cancelada.")
            return
        
        adicionar_novo_carro(ano, km, potencia, preco_real)

        print("\nIniciando retreinamento do modelo com os dados atualizados...")
        try:
            treinar_modelo()

        except Exception as e:
            print(f"\n[Erro ao retreinar]: {e}")
    else:
        print("\nSaindo do sistema.")

if __name__ == "__main__":
    menu_interativo()
            
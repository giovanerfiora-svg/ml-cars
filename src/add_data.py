import csv
import os
from train import treinar_e_salvar_modelo

def adicionar_novo_dado():
    diretorio_script = os.path.dirname(os.path.abspath(__file__))
    raiz_projeto = os.path.dirname(diretorio_script)
    caminho_csv = os.path.join(raiz_projeto, "data", "cars.csv")

    print("========================================")
    print("   SISTEMA DE GESTÃO E RETREINAMENTO    ")
    print("========================================")
    print("1. Adicionar novo dado real ao dataset")
    print("2. Sair\n")

    opcao = input("Escolha uma opção (1 ou 2): ")

    if opcao == "1":
        try:
            ano = int(input("Ano: "))
            km = float(input("Quilometragem: "))
            potencia = float(input("Potência do motor: "))
            preco = float(input("Preço real de venda (R$): "))

            with open(caminho_csv, mode='a', newline='', encoding='utf-8') as arquivo:
                escritor = csv.writer(arquivo)
                escritor.writerow([ano, km, potencia, preco])

            print(f"\n[Sucesso] Novo registro adicionado ao arquivo '{caminho_csv}'!\n")
            print("Iniciando retreinamento do modelo e atualizando o arquivo salvo...")
            
            treinar_e_salvar_modelo()

        except ValueError:
            print("\n[Erro] Dados inválidos digitados. Tente novamente.")
    else:
        print("\nSaindo...")

if __name__ == "__main__":
    adicionar_novo_dado()
# Estimador de Preço de Carros Usados (Machine Learning)

Este é um projeto prático e evolutivo desenvolvido com o objetivo de aprender e aplicar os **fundamentos de Machine Learning e Engenharia de Dados** utilizando Python.

O sistema utiliza um modelo de regressão para estimar o preço de veículos com base em suas características físicas e histórico de uso, além de permitir retreinamento contínuo com novos dados inseridos.

---

## Funcionalidades

- **Carga e Tratamento de Dados:** Leitura e estruturação automatizada de datasets em formato CSV usando `pandas`.
- **Treinamento e Avaliação:** Treinamento de modelo com divisão entre conjunto de Treino (75%) e Teste (25%).
- **Interface Interativa (CLI):** Estimativa de preços em tempo real no terminal com base em entradas do usuário.
- **Feedback Loop & Retreinamento:** Inserção de novas vendas reais com atualização e recalibragem automática dos pesos do modelo.
- **Análise Gráfica:** Diagnóstico visual da qualidade das previsões e distribuição dos resíduos/erros via `matplotlib`.

---

## Análise Gráfica do Modelo

Abaixo está o diagnóstico visual gerado pelo script `visualization.py`, mostrando a proximidade das previsões com a linha perfeita e a distribuição dos erros:

![Gráfico de Análise de Previsões e Resíduos](assets/grafico_residuos.png)

---

## Conceitos Aprendidos na Prática

1. **Supervised Learning (Regressão):** Uso do algoritmo `LinearRegression` para prever um valor numérico contínuo ($y = \text{Preço}$) a partir de atributos ($X = \text{Ano, Km, Potência}$).
2. **Qualidade de Dados vs. Desempenho:** Aumento substancial da métrica de determinação ($R^2$) de valores negativos para **~0.96** ao expandir a amostra de dados inicial e eliminar ruídos.
3. **Métricas de Avaliação de Regressão:**
   - **MAE (Erro Médio Absoluto):** Medida do erro direto em Reais (R$).
   - **RMSE (Raiz do Erro Quadrático Médio):** Penalização de grandes desvios.
   - **$R^2$ Score:** Capacidade explicativa do modelo sobre a variação dos dados.
4. **Resíduos & Viés:** Identificação de padrões de erro através de histogramas e scatter plots.
5. **Prevenção de Overfitting/Underfitting:** Separação rígida de dados usando `train_test_split`.

---

## Estrutura do Repositório

```text
ml-cars/
├── assets/
│   └── grafico_residuos.png # Gráfico exportado de análise de desempenho
├── data/
│   └── cars.csv           # Dataset tabular com histórico de veículos
├── src/
│   ├── load_data.py       # Leitura e inspeção do dataset com Pandas
│   ├── train.py           # Treinamento do modelo básico de Regressão Linear
│   ├── evaluate.py        # Divisão treino/teste e cálculo das métricas
│   ├── predict.py         # Interface CLI para novas previsões
│   ├── add_data.py        # Coleta de novos dados e retreinamento automático
│   └── visualization.py   # Geração de gráficos de análise de erro (Matplotlib)
├── .gitignore             # Arquivos e pastas ignorados pelo Git
├── requirements.txt       # Dependências e bibliotecas do projeto
└── README.md              # Documentação principal
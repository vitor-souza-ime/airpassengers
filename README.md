# 📊 AirPassengers – Modelagem SARIMA

Repositório: [https://github.com/vitor-souza-ime/airpassengers](https://github.com/vitor-souza-ime/airpassengers)
Arquivo principal: `main.py`

---

## 📌 Descrição

Este projeto realiza a modelagem e previsão da série temporal **AirPassengers** utilizando o modelo **SARIMA (Seasonal ARIMA)** com a biblioteca `statsmodels` em Python.

O conjunto de dados contém o número mensal de passageiros aéreos internacionais entre **janeiro de 1949 e dezembro de 1960**, sendo um benchmark clássico em análise de séries temporais.

O script contempla:

* 📈 Visualização da série temporal
* 🔍 Decomposição sazonal (modelo multiplicativo)
* ✂️ Separação em treino e teste
* 🧠 Ajuste de modelo SARIMA
* 🔮 Geração de previsão
* 📊 Avaliação com RMSE
* 📉 Visualização comparativa (real vs previsto)

---

## 🧰 Tecnologias Utilizadas

* Python 3.x
* pandas
* numpy
* matplotlib
* statsmodels
* scikit-learn

---

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/vitor-souza-ime/airpassengers.git
cd airpassengers
```

Instale as dependências:

```bash
pip install statsmodels pandas numpy matplotlib scikit-learn
```

---

## ▶️ Execução

Execute o arquivo principal:

```bash
python main.py
```

O script irá:

1. Baixar automaticamente o dataset AirPassengers
2. Exibir gráfico da série temporal
3. Mostrar a decomposição sazonal
4. Ajustar modelo SARIMA(1,1,1)(1,1,1,12)
5. Exibir o valor do RMSE
6. Mostrar gráfico final com previsão

---

## 🧠 Modelo Utilizado

Modelo configurado:

* **Ordem não sazonal:** (1,1,1)
* **Ordem sazonal:** (1,1,1,12)
* **Período sazonal:** 12 meses

A decomposição é feita com modelo multiplicativo, apropriado para séries com variância crescente.

---

## 📊 Métrica de Avaliação

A performance é avaliada utilizando:

* **RMSE (Root Mean Squared Error)**

O conjunto de teste corresponde aos últimos 12 meses da série.

---

## 📁 Estrutura do Projeto

```
airpassengers/
│
├── main.py
└── README.md
```

---

## 📚 Referências Teóricas

* Box, G. E. P., & Jenkins, G. M. (1970)
* Hyndman, R. J., & Athanasopoulos, G. (2018)
* Brockwell, P. J., & Davis, R. A. (2016)
* Chatfield, C. (2003)

---

## 👨‍🏫 Autor

Vitor Amadeu Souza
Professor e Pesquisador

---

## 📌 Observações

* O dataset é carregado diretamente de uma fonte pública.
* O projeto pode ser expandido com:

  * Análise de resíduos
  * Intervalos de confiança
  * Testes de estacionariedade (ADF)
  * Comparação com outros modelos (ETS, Prophet, etc.)


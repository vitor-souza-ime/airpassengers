# ==========================================================
# 1) Instalação
# ==========================================================
!pip install statsmodels --quiet

# ==========================================================
# 2) Importações
# ==========================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error

plt.style.use('seaborn-v0_8')

# ==========================================================
# 3) Carregando AirPassengers (fonte pública)
# ==========================================================
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
data = pd.read_csv(url)

data.columns = ['Month', 'Passengers']
data['Month'] = pd.to_datetime(data['Month'])
data.set_index('Month', inplace=True)

print(data.head())

# ==========================================================
# 4) Gráfico da Série
# ==========================================================
plt.figure(figsize=(12,5))
plt.plot(data, label='Número de Passageiros')
plt.title('AirPassengers (1949-1960)')
plt.xlabel('Ano')
plt.ylabel('Passageiros')
plt.legend()
plt.grid()
plt.show()

# ==========================================================
# 5) Decomposição
# ==========================================================
decomposition = seasonal_decompose(data['Passengers'], model='multiplicative', period=12)
decomposition.plot()
plt.show()

# ==========================================================
# 6) Separando treino e teste
# ==========================================================
train = data.iloc[:-12]
test = data.iloc[-12:]

# ==========================================================
# 7) Modelo SARIMA
# ==========================================================
model = SARIMAX(train,
                order=(1,1,1),
                seasonal_order=(1,1,1,12))

results = model.fit()

# ==========================================================
# 8) Previsão
# ==========================================================
forecast = results.get_forecast(steps=12)
forecast_mean = forecast.predicted_mean

# ==========================================================
# 9) Avaliação
# ==========================================================
rmse = np.sqrt(mean_squared_error(test, forecast_mean))
print(f"RMSE: {rmse:.2f}")

# ==========================================================
# 10) Gráfico Final
# ==========================================================
plt.figure(figsize=(12,5))
plt.plot(train.index, train, label='Treino')
plt.plot(test.index, test, label='Real')
plt.plot(test.index, forecast_mean, label='Previsão', linestyle='--')

plt.title('Previsão SARIMA - AirPassengers')
plt.xlabel('Ano')
plt.ylabel('Passageiros')
plt.legend()
plt.grid()
plt.show()

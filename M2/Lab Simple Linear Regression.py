# -*- coding: utf-8 -*-
"""Simple Linear Regression

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fJM7ZmJBfKqamERwI5c0_bv4AzJ6pyFI
"""

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
# %matplotlib inline //Configura o ambiente para que os gráficos gerados pelo matplotlib sejam exibidos diretamente abaixo das células de código quando são renderizados, sem a necessidade de utilizar plt.show() explicitamente para exibir os gráficos.

!wget -O FuelConsumption.csv https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv

df = pd.read_csv("FuelConsumption.csv")

df.head()

"""Criar novo dataframe a partir do dataframe original, exibindo apenas as 9 primeiras linhas"""

cdf = df[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB', 'CO2EMISSIONS']]
cdf.head(9)

"""Plotar cada uma das features."""

viz = cdf[['CYLINDERS', 'ENGINESIZE',  'CO2EMISSIONS', 'FUELCONSUMPTION_COMB']]
viz.hist()
plt.show()

"""Representar graficamente cada uma das características em relação à Emissão, para ver quão linear é a relação."""

plt.scatter(cdf.FUELCONSUMPTION_COMB, cdf.CO2EMISSIONS, color = 'blue')
plt.xlabel("FUELCONSUMPTION_COMB")
plt.ylabel("Emission")
plt.show()

plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS, color = 'blue')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()

plt.scatter(cdf.CYLINDERS, cdf.CO2EMISSIONS, color = 'blue')
plt.xlabel("Cylinders")
plt.ylabel("Emission")
plt.show()

msk = np.random.rand(len(df)) < 0.8 # Cria uma série de números aleatórios com o mesmo tamanho (número de linhas) do DataFrame df. Cada número representa uma chance de ser escolhido para o conjunto de treino ou teste.
train = cdf[msk]
test = cdf[~msk]

plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS, color = 'blue')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()

from sklearn import linear_model
regr = linear_model.LinearRegression() # Modelo de RL em linha reta que tenta se ajustar aos dados de maneira que possa prever valores futuros com base nos padrões observados nos dados de treinamento.
train_x = np.asanyarray(train[['ENGINESIZE']])
train_y = np.asanyarray(train[['CO2EMISSIONS']])
regr.fit(train_x, train_y) # Treinamento do modelo de regressão linear.
# The coefficients
print ('Coefficients: ', regr.coef_)
print ('Intercept: ',regr.intercept_)

plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')
plt.plot(train_x, regr.coef_[0][0]*train_x + regr.intercept_[0], '-r')
plt.xlabel("Engine size")
plt.ylabel("Emission")

from sklearn.metrics import r2_score

test_x = np.asanyarray(test[['ENGINESIZE']])
test_y = np.asanyarray(test[['CO2EMISSIONS']])
test_y_ = regr.predict(test_x)

print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_ - test_y)))
print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_ - test_y) ** 2))
print("R2-score: %.2f" % r2_score(test_y , test_y_) )

train_x = train[["FUELCONSUMPTION_COMB"]]

test_x = test[["FUELCONSUMPTION_COMB"]]

regr = linear_model.LinearRegression()

regr.fit(train_x, train_y)

"""Encontrar previsões usando a função de previsão do modelo e os dados"""

predictions = regr.predict(test_x)

print("Mean absolute error: %.2f" % np.mean(np.absolute(predictions - test_y)))
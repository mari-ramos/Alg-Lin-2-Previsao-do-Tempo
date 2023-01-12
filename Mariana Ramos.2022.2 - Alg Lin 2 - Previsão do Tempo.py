import pandas as pd
import numpy as np
from pathlib import Path  
from sklearn.metrics import accuracy_score #acuracia
from sklearn.metrics import precision_score #precision
from sklearn.metrics import r2_score

train = pd.read_csv('weatherAUS_training.csv') #chamada para ler o arquivo csv no pandas
test = pd.read_csv('weatherAUS_testing.csv')

train.drop(columns=["Date", "Location"], inplace=True) #tirar colunas de data e localização
train.fillna(0, inplace=True) #substituir os valores de na por zero 
train.replace(('Yes','No'),(1,0),inplace=True) #substituir yes por 1 e no por 0
train.replace(('N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW'),(0, 22.5, 45, 72.5, 90, 112.5, 135, 157.5, 180, 202.5, 225, 247.5, 270, 292.5, 315, 337.5),inplace=True)
#substituir os valores de direção do vento por seus angulos

y_train = train["RainTomorrow"].values #coloco em uma variavel apenas os valores de RainTomorrow
x_train = train.drop(columns=["RainTomorrow"]).values #coloco em uma variaveel todos os valores de todas a s colunas, menos o RainTomorrow
coefficients = np.linalg.inv(x_train.T.dot(x_train)).dot(x_train.T).dot(y_train) #formula dos minimos quadrados aplicada usando numpy


y_predict = np.dot(x_train, coefficients) 

train['RainTomorrow_predict'] = y_predict

def chuva(x): #para valores maiores ou iguais a 0.5 o programa denomina como um Sim (terá ocorrência de chuvas), para valores menores que 0.5 o programa denomina como Não (sem ocorrência de chuvas)
  if(x >= 0.5):
    return 1
  else:
    return 0

train['RainTomorrow_predict'] = train['RainTomorrow_predict'].transform(chuva)

print(train)

'''filepath = Path('train.csv')  #codigo para salvar o arquivo atualizado, com a coluna de predição
filepath.parent.mkdir(parents=True, exist_ok=True)  
train.to_csv(filepath)'''

'''acuracia_train = accuracy_score(train['RainTomorrow'],train['RainTomorrow_predict']) #acurácia para o arquivo de treinamento
print('Acurácia: %f'% acuracia_train)'''

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

test.drop(columns=["Date", "Location"], inplace=True)
test.fillna(0, inplace=True)
test.replace(('Yes','No'),(1,0),inplace=True)
test.replace(('N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW'),(0, 22.5, 45, 72.5, 90, 112.5, 135, 157.5, 180, 202.5, 225, 247.5, 270, 292.5, 315, 337.5),inplace=True)

test['RainTomorrow'] = np.concatenate([test['RainToday'].values[1:], [0]]) #valor qualquer para preencher a ultima linha da coluna criada baseada na coluna RainToday do proprio arquivo de teste
test['RainTomorrow']

y_test = test["RainTomorrow"].values
x_test = test.drop(columns=["RainTomorrow"]).values

y_test_predict = np.dot(x_test, coefficients) #multiplicação dos dados de entrada do teste com o coeficiente achado através dos dados de treinamento utilizando o numpy para achar o dado de saida do teste

test['RainTomorrow_predict'] = y_test_predict
test['RainTomorrow_predict'] = test['RainTomorrow_predict'].transform(chuva)

'''filepath = Path('test.csv')  #criação do arquivo atualizado com a coluna de predição/solução
filepath.parent.mkdir(parents=True, exist_ok=True)  
test.to_csv(filepath)'''

print(test)
print(coefficients) #print dos coeficientes/parâmetros

r2 = r2_score(y_test, y_test_predict)
print(r2) #r2 da prediçao do teste

precision = precision_score(test['RainTomorrow'],test['RainTomorrow_predict']) #precisao do metodo
print('Precisão: %f' % precision)

acuracia_test = accuracy_score(test['RainTomorrow'],test['RainTomorrow_predict']) #acuracia do metodo
print('Acurácia: %f'% acuracia_test)
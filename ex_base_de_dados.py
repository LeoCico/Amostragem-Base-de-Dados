import pandas as pd
import numpy as np
import random
from sklearn.model_selection import StratifiedShuffleSplit

dataset = pd.read_csv('credit_data.csv')


# AMOSTRAGEM ALEATORIA SIMPLES


def amostragem_aleatoria_simples(dataset, amostras):
    df_dataset = dataset.sample(n=amostras, random_state=1)
    return df_dataset.head()


amostragem_aleatoria_simples(1000)


# AMOSTRAGEM POR GRUPOS (GRUPOS)


def amostragem_grupos(dataset, grupos):

  intervalo = len(dataset) // grupos
  soma = 0
  grupo = []
  id_grupo = 0

  for _ in dataset.iterrows():
    grupo.append(id_grupo)
    soma += 1
    if soma >= intervalo:
      soma = 0
      id_grupo += 1

  dataset['grupo'] = grupo
# return dataset.tail()

  selecao = random.randint(0, grupos -1)
  return dataset[dataset['grupo'] == selecao]


amostragem_grupos(dataset, 1000)


# AMOSTRAGEM SISTEMATICA


def amostragem_sistematica(dataset, divisor):
  intervalo_sistematica = len(dataset) // divisor
  inicio = random.randint(0, intervalo_sistematica)
  valores = np.arange(inicio, len(dataset), step=intervalo_sistematica)
  valores = valores.tolist()
  df_amostragem = dataset.iloc[valores]
  return df_amostragem


amostragem_sistematica(dataset,100)


# AMOSTRAGEM ESTRATIFICADA


def amostragem_estratificada(dataset, percentual):
  dataset['c#default'].value_counts()
  split = StratifiedShuffleSplit(test_size=percentual, random_state=1)
  for x, y in split.split(dataset, dataset['c#default']):
    df_x = dataset.iloc[x]
    df_y = dataset.iloc[y]
  return df_y['c#default'].value_counts()


amostragem_estratificada(dataset, 100 / len(dataset))


# AMOSTRAGEM RESERVATORIO serve pra voce usar em bases que estao em constante mudança


def amostragem_reservatorio(dataset, amostras):
  stream = []

  for x in range(len(dataset)):
    stream.append(x)

  reservatorio = [0] * amostras

  for x in range(amostras):
    reservatorio[x] = stream[x]

  while x <= len(dataset):
    a = random.randrange(0, x + 1)
    if a < amostras:
      reservatorio[a] = stream[x]
    x += 1

  return dataset.iloc[reservatorio]


amostragem_reservatorio(dataset,100)

a = amostragem_reservatorio(dataset, 100)
b = amostragem_sistematica(dataset, 100)
c = amostragem_estratificada(dataset, 100)
d = amostragem_grupos(dataset, 100)
e = amostragem_aleatoria_simples(dataset, 100)

dataset['age'].mean()
a['age'].mean()
b['age'].mean()
c['age'].mean()
d['age'].mean()
e['age'].mean()

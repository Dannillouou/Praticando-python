import pandas as pd

import numpy as np
import time

def calcular_quarado(numero):
    return numero ** 2

lista_loop = list(range(1,11))
array_loop = np.array(range(1,11))
series_loop = pd.Series(range(1,11))

# vetorizando função
# a função vetorizada passa a poder ser utilizada iterando por vetores 
# pois a função é invocada para cada elemento e um conjunto de dados
funcao_vetorizada = np.vectorize(calcular_quarado)

print(time.time())
print(type(lista_loop), funcao_vetorizada(lista_loop))
print(time.time())

print(time.time())
print(type(array_loop), funcao_vetorizada(array_loop))
print(time.time())

print(time.time())
print(type(series_loop), funcao_vetorizada(series_loop))
print(time.time())
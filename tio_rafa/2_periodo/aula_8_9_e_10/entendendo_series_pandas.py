import numpy as np
import pandas as pd

# estruturas de dados iniciais
lista_1 = [1, 2, 3, 4, 5]
lista_2 = ["I", "II", "III", "IV", "V"]

dicionario_1 = dict(zip(lista_1, lista_2))

ndarray_1 = np.array(lista_1)

print(lista_1)
print(lista_2)
print(ndarray_1)
print(dicionario_1)

print("#"*80)

serie_1 = pd.Series(lista_1)
print("\nLista 1: ", serie_1, sep="\n")

serie_1 = pd.Series(lista_2)
print("\nLista 2: ", serie_1, sep="\n")

# relembrar é viver, ou não
print("\nSerie Shape: ", serie_1.shape)
# shape e values são os atributos do array que armazena os valores
print("\nSerie Values: ", serie_1.values)
print("Ser inedxes", serie_1.index)

serie_1 = pd.Series(lista_1, lista_2)
# o parametro passado primeiro é o valor e o segundo os indices
print("\nLista 1 e lista 2: ", serie_1, sep="\n")

serie_1 = pd.Series(dicionario_1)
# inverte a ordem em relação à criação anterior
print("\nDicionario 1: ", serie_1, sep="\n")

serie_1 = pd.Series(ndarray_1, lista_2)
print("\nNDarray 1 e lista 2: ", serie_1, sep="\n")

print("\nNumPy para lista: ", ndarray_1.tolist())
print("\nSerie para NumPy: ", serie_1.to_numpy())
# aparentemente numpy é um método
print("\nSerie para lista: ", serie_1.to_list())
print("\nSerie para lista: ", serie_1.to_list())
# metodo to list do ndarray
print("\nSerie para lista: ", serie_1.tolist())

print("#"*80)

# acessando elementos na série

# acessando os tres primeiros elementos 
# os indices sao indexados
print("\n Acessando elementos com slice: ", serie_1[:3], sep = "\n")
print("Acessando os elementos com head", serie_1.head(3), sep = "\n")

# acessando os tres primeiros elementos, de baixo para cima
print("\nAcessandos os elementos com slice: ", serie_1[-3:], sep = "\n")
print("Acessandos os elementos com tail: ", serie_1.tail(3), sep = "\n")

#acessando elemento especifico
print("\nAcessando via rótulo: ", serie_1[0]) # indice como em array
print("Acessando via rótulo: ", serie_1["I"]) # indice especifico

# indices especificicos
print("\nIndex Max: ", serie_1.idxmax())
print("Index Min: ", serie_1.idxmin())

print("#"*80)

# usando métodos para localizar ao inves de indices

# localizando pelo indice personalizado
print("\nLOC: ", serie_1.loc["I": "III"], sep="\n")
# localizando pelo indice real
print("\nILOC: ", serie_1.iloc[0:3], sep="\n")
# apesar de localizar pelo indice real, mantem o indice personalizado no
# indice

# forma de escrever numeros que so o python aceita
# portanto, NAO USE
dicionario_2 = {"I":10, "II":42, "III":7, "V":1_000_000}
dicionario_3 = {"I":1, "II":12, "III":13, "IV":0}

serie_2 = pd.Series(dicionario_2)
serie_3 = pd.Series(dicionario_3)

print("\nDicionario 2: ", serie_2, sep="\n")
print("\nDicionario 3: ", serie_3, sep="\n")
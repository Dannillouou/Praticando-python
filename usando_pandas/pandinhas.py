import pandas as pd

# usando numeros aleatorios para fazer um dataframe
import random

#usando o alfabeto
import string

# mudando pasta de trabalho
import os
os.chdir("usando_pandas")

#=======================================================================
# # series in pandas
# serie = [1, 7, 2, 42, 8, 7, 90, 41]

# # funciona como uma espécie de lista
# variavel = pd.Series(serie)

# # é possível iterar sobre
# for valor in variavel:
#   print(valor)

# alfabeto = list(string.ascii_lowercase)

# # é possível mudar os labels de cada valor
# variavel = pd.Series(serie, index = alfabeto[0:len(variavel)])

# # funciona como um dicionario
# # aceita dicionario como entrada para fazer uma series
# calorias = {"day1": 300, "day2":250, "day3": 325}
# variavel = pd.Series(calorias)

# # especificando somente os indices que quisermos
# variavel = pd.Series(calorias, index = ["day1", "day2"])

# # em pandas os datasets são chamados dataframes e são
# # a junção de várias séries, cada série sendo uma coluna
# lista_calorias = []
# lista_duracao = []
# lista_labels = []

# for i in range(100):
#   lista_calorias.append(random.randint(250,500))
#   lista_duracao.append(random.randint(15,150))
#   lista_labels.append("Dia " + str(i))

# dados_exercicio = {
#   "calories": lista_calorias,
#   "duration": lista_duracao
# }

# print("\n")

# print(variavel)

# #=======================================================================
# # um DataFrame é um array bidimensional com linhas e colunas

# print(pd.DataFrame(dados_exercicio))

# # mudando labels do dataframe
# dataframe = pd.DataFrame(dados_exercicio, index=lista_labels)

# # pandas usa o atributo loc para retornar uma ou mais
# # colunas específicadas
# # retorna uma serie em panda
# print("Usando o loc")

# print(dataframe.loc["Dia 0"]) # printa informações da linha

# print(dataframe.loc[["Dia 0", "Dia 1", "Dia 2", "Dia 3", "Dia 4", "Dia 5", "Dia 6", "Dia 7", "Dia 8", "Dia 9"]]) # printa a lista de linhas

#=======================================================================
# lendo arquivo .csv

mtcars = pd.read_csv("mtcars.csv")
# aparentemente o panda chama o metodo to string quando o dataframe é chamado em um print

#=======================================================================
# lendo arquivo .json

pokedex = pd.read_json("pokedex.json")

#=======================================================================
# analisando o dataframe

#informações sobre o dataframe, do objeto DataFrame
# printa o objeto na memória, a quantidade de linhas, informações sobre cada coluna:
# nome da variável, se tem (e quantos são) dados nulos e o tipo armazenado na coluna
mtcars.info()
pokedex.info()

# primeiras linhas
# print(pokedex.head(10))# primeiras 10 linhas

# útlimas linhas
# print(mtcars.tail(10))# últimas 10 linhas

#=======================================================================
# não fiz nenhum procedimento de limpeza de base de dados para linhas vazias
# porque nenhum dos dois dataframes tem esse problema

print(mtcars["cyl"].mean())
print(mtcars["cyl"].median())
print(mtcars["cyl"].mode()[0])

# vendo duplicatas
print("vendo duplicatas")
print(mtcars.duplicated())

# removendo duplicatas
# (não vai funcionar pra esse dataframe)
mtcars.drop_duplicates(inplace = True)
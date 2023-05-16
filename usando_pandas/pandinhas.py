import pandas as pd

#usando o alfabeto
import string

# dataframe = pd.read_csv("mtcars.csv")
# print(dataframe)
# print(dataframe.to_string())
# aparentemente o panda chama o metodo to string quando o dataframe é chamado em um print

# series in pandas
serie = [1, 7, 2, 42, 8, 7, 90, 41]

# funciona como uma espécie de lista
variavel = pd.Series(serie)

# é possível iterar sobre
for valor in variavel:
    print(valor)

alfabeto = list(string.ascii_lowercase)

# é possível mudar os labels de cada valor
variavel = pd.Series(serie, index = alfabeto[0:len(variavel)])

# funciona como um dicionario
# aceita dicionario como entrada para fazer uma series
calorias = {"day1": 300, "day2":250, "day3": 325}
variavel = pd.Series(calorias)

# especificando somente os indices que quisermos
variavel = pd.Series(calorias, index = ["day1", "day2"])

# em pandas os datasets são chamados dataframes e são
# a junção de várias séries, cada série sendo uma coluna

dados_exercicio = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

variavel = pd.DataFrame(dados_exercicio)

print("\n")

print(variavel)
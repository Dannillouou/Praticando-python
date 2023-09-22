import numpy as np
import pandas as pd

print("##### Criando DATAFRAMES #####")

indices = ["The Pacific", "Black Mirror", "CSI", "NCIS", "Lost"]
colunas = ["Nota", "Temporadas", "Episódios"]
dados = [[8.3, 1, 10], [8.3, 6, 27], [7.7, 15, 337], [6.9, 14, 458], [8.3, 6, 121]]
df = pd.DataFrame(dados, index=indices, columns=colunas)

print(df, end="\n\n")

#=========================================================================
print("##### Seleção #####")
print("Notas: ")
print(df["Nota"], end="\n\n")
print(df[["Temporadas", "Episódios"]], end="\n\n")

#=========================================================================
print("##### Loc ILOC #####")
print("Lost: ")
# localizador por rotulo
print(df.loc["Lost"], end="\n\n") 
# localizando primeiro índice
print(df.iloc[0], end="\n\n") 

#=========================================================================
print("##### Seleção combinada #####")
# buscando uma lista de indices
print(df.loc[["The Pacific", "NCIS"], "Temporadas"], end="\n\n")
# buscando tempradas e nota para todos os índices
print(df.loc[:, ["Temporadas", "Nota"]], end="\n\n")

#=========================================================================
# print(type(df.loc[:, [""]]))

print(df.columns)
print(type(df.columns))
print(df.columns.values)
print(type(df.columns.values))

print(df.index)
print(type(df.index))
print(df.index.values)
print(type(df.index.values))

# criando nova coluna no df
df["Coluna extra"] = df["Nota"]
print(df, end ="\n\n")

# retirando coluna
df.drop("Coluna extra", axis=1, inplace=True)
print(df, end="\n\n")

# retirando por indice
df.drop("Lost", axis=0, inplace=True)
print(df, end="\n\n")

print(df.shape)# (4, 3)

#=========================================================================
print("##### SELEÇÃO CONDICIONAL #####")

print(df[df["Nota"] > 8])
# coloca True em todos os dados do df maiores que 3
print(df>3)
print(df[df>3]) # os valores menores que 3 fica como NaN

#=========================================================================
print("##### SELEÇÃO CONDICIONAL + MÚLTIPLA #####")

# temporadas das séries com nota acima de 8
print(df[df["Nota"] > 8]["Temporadas"]) 
# temporadas e episódios das séries com nota acima de 8
print(df[df["Nota"] > 8][["Temporadas", "Episódios"]])

print(df[(df["Nota"] > 8) & (df["Temporadas"]>3)]) 
print("Hello world")
print(df)

import pandas as pd
from entendendo_series_pandas import serie_1, serie_2, serie_3


resultado = serie_2.add(serie_3)
print("\n Serie add ", resultado, sep="\n")

resultado = serie_2.sub(serie_3)
print("\n Serie sub ", resultado, sep="\n")

print("Série Count: ", resultado.count())
print("Série Size: ", resultado.size)

dicionario_4 = {"v": 42}

# concatenando series
serie_4 = pd.Series(dicionario_4)
print("\n Concatenação ", pd.concat([serie_3, serie_4]), sep="\n")
print("Série Count: ", resultado.count())
print("Série Size: ", resultado.size)

# preenchendo buracos com 0
resultado = serie_2.add(serie_3, fill_value = 0)
print("\n Série Add: ", resultado, sep="\n")
print("Série Count: ", resultado.count())
print("Série Size: ", resultado.size)

# dropando buracos
resultado = serie_2.add(serie_3)
resultado.dropna(inplace = True) # separando um statement por linha
print("\n Série Add: ", resultado, sep="\n")
print("Série Count: ", resultado.count())
print("Série Size: ", resultado.size)

# preenchendo buracos
resultado = serie_2.add(serie_3)
resultado.filna(42, inplace = True)
print("\n Série fill: ", resultado, sep="\n")
print("Série Count: ", resultado.count())
print("Série Size: ", resultado.size)
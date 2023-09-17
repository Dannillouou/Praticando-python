import numpy as np
import pandas as pd

serie_1 = pd.Series(np.random.randint(0, 100, size=10))
serie_2 = pd.Series(np.random.randint(0, 10, size=10))
serie_3 = pd.Series(np.random.randint(0, 10, size=10))

# print(serie_1)

# questao 1
desvio_padrao = serie_1.std()
media = serie_1.mean()

# questao 2
print(serie_1.value_counts())

# questao 3
print(serie_1.loc[serie_1%5 == 0].index)

# questao 4
print(serie_1.loc[serie_1.isin(serie_2)])

# questao 5
contagens = serie_1.value_counts()
filtro = contagens.loc[contagens == 1].index
serie_1.loc[serie_1.isin(filtro)] = "Desconsiderar"
print(serie_1)

# questao 6
print(set(serie_3.loc[~serie_3.isin(serie_2)].to_list()))
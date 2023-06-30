# Exemplo 6

import pandas as pd

from bokeh.models import ColumnDataSource
from bokeh.sampledata.periodic_table import elements

pd.set_option("display.max_columns", None)
print(elements.head())
print(elements.count())
print(elements)

# retirando elementos na
elements.dropna(inplace=True)

# print(elements.head())
# print(elements.count())
# print(elements)
# sobraram 31 elementos

# dicionário que faz a correspondência de estado para cor
color_dict = {"gas" : "green", "liquid" : "blue", "solid" : "grey"}

# lista para criar a coluna de cores no dataset
colors = []

# fazendo correspondencia de cor com estado padrão do elemento
for each_element in elements["standard state"]:
    colors.append(color_dict[each_element])
    
# adicionando coluna com as cores
elements["colors"] = colors

# criando nova coluna com ajuste do raio de van der Waals
elements["size"] = elements["van der Waals radius"] / 10

print(elements.head())

elements[elements["standard state"] == "gas"]

# criando os ColumnDataSources
gas = ColumnDataSource(elements[elements["standard state"] == "gas"])
liquid = ColumnDataSource(elements[elements["standard state"] == "liquid"])
solid = ColumnDataSource(elements[elements["standard state"] == "solid"])
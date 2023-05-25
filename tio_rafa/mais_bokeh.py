from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from sklearn import datasets
import numpy as np

iris = datasets.load_iris()
# print(list(iris.keys()))

# pegando todas as linhas da
# segunda coluna
x = iris.data[:, 2:3]
# terceira coluna
y = iris.data[:, 3:4]

# transformando em lista
# é um ndarray, uma lista de listas
# o concatenate pega todo o conteúdo de cada lista
# e concatena em um único ndarray, que o python transforma
# em lista com a função list()
x_flat = list(np.concatenate(x))
y_flat = list(np.concatenate(y))

# print(type(x_flat)) # lista

# saida da vis
output_file("iris.html")

# instanciando objeto do tipo figura
# que faz o plot do gráfico
figure = figure()
figure.circle(x_flat, y_flat)

figure.width = 1280
figure.height = 720
figure.background_fill_color = "#558833"
figure.background_fill_alpha = 0.5

show(figure)
# css zen garden
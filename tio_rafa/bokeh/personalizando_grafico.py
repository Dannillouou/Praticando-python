from bokeh.plotting import figure
from bokeh.models import Range1d
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

# Tamanho da figura
figure.width = 1280
figure.height = 720
figure.background_fill_color = "#CABDFD"
figure.background_fill_alpha = 0.5

# Texto do título
figure.title.text = "Correlação Comprimento Largura"
figure.title.text_color = "DeepPink"
figure.title.text_font = "fantasy"
figure.title.text_font_size = "42px"
figure.title.align = "center"

# Eixos
# Rótulo do eixo
figure.xaxis.axis_label = "Petal Length"
# Cor dos pauzinhos
figure.xaxis.minor_tick_line_color = "green"
# Tamanho dos pauzinho para dentro
figure.xaxis.minor_tick_in = 15
# Direção dos valores no eixo
figure.xaxis.major_label_orientation = "vertical"
# retirando os eixos
# figure.xaxis.visible = False

# Rótulo do eixo
figure.yaxis.axis_label = "Petal Width"
# Cor dos pauzinhos
figure.yaxis.minor_tick_line_color = "green"
# Tamanho dos pauzinho para dentro
figure.yaxis.minor_tick_in = 15
# Direção dos valores no eixo
figure.yaxis.major_label_orientation = "vertical"
# retirando os eixos
# figure.yaxis.visible = False

# Cor do texto dos rótulos
figure.axis.axis_label_text_color = "blue"
# Cor dos valores nos eixos
figure.axis.major_label_text_color = "orange"

# Geometria dos eixos
figure.x_range = Range1d(start = 0, end = 10)
figure.y_range = Range1d(start = 0, end = 5)

# Ajustando limites dos eixos
figure.xaxis.bounds = (0, 2)
figure.yaxis.bounds = (1, 3)

figure.xaxis[0].ticker.desired_num_ticks = 4
figure.yaxis[0].ticker.desired_num_ticks = 4

figure.xaxis[0].ticker.num_minor_ticks = 4
figure.yaxis[0].ticker.num_minor_ticks = 4

# Grid
# figure.xgrid.grid_line_color = None
# figure.ygrid.grid_line_color = None
figure.xgrid.grid_line_color = "DeepPink"
# figure.xgrid.grid_line_alpha = 0.8
figure.ygrid.grid_line_color = "DeepPink"
# figure.ygrid.grid_line_alpha = 0.8

#
# figure.grid.grid_line_dash = [1, 42]# espaços, traços
figure.grid.grid_line_dash = "dashdot"

show(figure)
# css zen garden
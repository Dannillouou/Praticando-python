# Plot de dataset curioso feito em parceria com Luís Felipe de Abreu Marciano
from bokeh.plotting import figure

from bokeh.io import curdoc, show, save, output_file
from bokeh.models import ColumnDataSource, Grid, HBar, LinearAxis, Plot

# from bokeh.models import Range1d
# from bokeh.io import output_file, save, show
from sklearn import datasets
import numpy as np
import pandas as pd
import os

os.chdir("tio_rafa")

# saida da vis
output_file("curioso.html")

felicidade = pd.read_csv("./2018.csv")

subset = felicidade.head(30)
print(subset)

quantidade_paises = len(subset.index)
# y = (subset["Country or"].min(), subset["Overall rank"].max(), quantidade_paises)
y = list(subset.iloc[0:31]["Country or region"])
x = list(subset.iloc[0:31]["Score"])

figure = figure(x_range=x, height=350, title="Happines rank",
           toolbar_location=None, tools="")
figure.vbar(x = x, top = y)

# figure.width = 1280
# figure.height = 720

show(figure)

# source = ColumnDataSource(dict(y=y, right=x,))

# plot = Plot(
#     title=None, width=1280, height=720)

# glyph = HBar(y="y", right="right", left=0, height=0.5, fill_color="#b3de69")
# plot.add_glyph(source, glyph)

# xaxis = LinearAxis()
# plot.add_layout(xaxis, 'below')

# yaxis = LinearAxis()
# plot.add_layout(yaxis, 'left')

# plot.add_layout(Grid(dimension=0, ticker=xaxis.ticker))
# plot.add_layout(Grid(dimension=1, ticker=yaxis.ticker))

# curdoc().add_root(plot)

# show(plot)

# # # # # iris = datasets.load_iris()

# # # # # x = iris.data[:, 2:3]
# # # # # y = iris.data[:, 3:4]

# # # # # x_flat = list(np.concatenate(x))
# # # # # y_flat = list(np.concatenate(y))

# # # # # instanciando objeto do tipo figura
# # # # # que faz o plot do gráfico
# # # # figure = figure()
# # # # figure.circle(x_flat, y_flat)

# # # # # Tamanho da figura
# # # # figure.width = 1280
# # # # figure.height = 720

# # # # # Cor background
# # # # # figure.background_fill_color = "#87CEEB"
# # # # # Opacidade background
# # # # figure.background_fill_alpha = 0.5

# # # # # Texto do título
# # # # figure.title.text = "Correlação Curiosa"
# # # # figure.title.text_color = "#D9895B"
# # # # figure.title.text_font = "helvetica"
# # # # figure.title.text_font_size = "42px"
# # # # figure.title.align = "center"

# # # # # Eixos
# # # # # Rótulo do eixo
# # # # figure.xaxis.axis_label = "Dado curioso"
# # # # figure.xaxis.axis_label_text_font_size = "20px"
# # # # # Cor dos pauzinhos
# # # # figure.xaxis.minor_tick_line_color = "#362C59"
# # # # # Tamanho dos pauzinho para dentro
# # # # figure.xaxis.minor_tick_in = 2

# # # # # Rótulo do eixo
# # # # figure.yaxis.axis_label = "Dado curioso"
# # # # figure.yaxis.axis_label_text_font_size = "20px"
# # # # # Cor dos pauzinhos
# # # # figure.yaxis.minor_tick_line_color = "#362C59"
# # # # # Tamanho dos pauzinho para dentro
# # # # figure.yaxis.minor_tick_in = 2


# # # # # Cor do texto dos rótulos
# # # # figure.axis.axis_label_text_color = "#D95276"
# # # # # Cor dos valores nos eixos
# # # # figure.axis.major_label_text_color = "#D95276"

# # # # # Grid
# # # # figure.xgrid.grid_line_color = "#F2916D"
# # # # # # figure.xgrid.grid_line_alpha = 0.8
# # # # figure.ygrid.grid_line_color = "#F2916D"
# # # # # figure.ygrid.grid_line_alpha = 0.8

# # # # #
# # # # # figure.grid.grid_line_dash = [1, 42]# espaços, traços

# # # # show(figure)
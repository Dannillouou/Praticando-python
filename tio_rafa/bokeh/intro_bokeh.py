# fazer plots
from bokeh.plotting import figure
from bokeh.io import output_file, save, show

import pandas as pd


# mudando pasta de trabalho
import os
os.chdir("tio_rafa")

# dataframe
bachelors = pd.read_csv("bachelors.csv")
x = bachelors["Year"]
y = bachelors["Agriculture"]

output_file("line_plot.html")

figure = figure()

figure.line(x, y)

# figuras diferenciadas
# figure.circle(x, y)
# figure.triangle(x, y)

show(figure)
# save(figure)
import pandas as pd
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
import os

output_notebook()

os.chdir("usando_pandas")

mtcars = pd.read_csv("mtcars.csv")

# mtcars.plot_bokeh(
#     kind = "scatter",
#     x = "wt",
#     y = "mpg",
#     xlabel = "Peso",
#     ylabel = "Milhas por galão",
#     title = "Eficiência por peso de carros"
# )

# forma coreta
plot = figure(
    title = "Eficiência por peso de carros",
    x_axis_label = "Peso",
    y_axis_label = "Milhas por galão",
    width = 500
)

plot.scatter(x="wt", y="mpg", source=mtcars)

show(plot)
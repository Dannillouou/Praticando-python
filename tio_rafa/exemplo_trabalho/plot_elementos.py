from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from organizando_dados_elementos import gas, liquid, solid

# fazendo os plots
import os
os.chdir("tio_rafa/exemplo_trabalho")
output_file("periodic_table.html")

# para gases
plot = figure()
plot.xaxis.axis_label = "Atomic Radius"
plot.yaxis.axis_label = "Boiling Point"

plot.circle(x = "atomic radius", y = "boiling point", size = "size", color = "colors",fill_alpha = 0.13,legend_label = "Gas",source = gas)
plot.circle(x = "atomic radius", y = "boiling point", size = "size", color = "colors",fill_alpha = 0.13,legend_label = "Liquid",source = liquid)
plot.circle(x = "atomic radius", y = "boiling point", size = "size", color = "colors",fill_alpha = 0.13,legend_label = "Solid",source = solid)

show(plot)
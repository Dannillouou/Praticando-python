from bokeh.layouts import gridplot
from bokeh.models.annotations import Span, BoxAnnotation
from bokeh.plotting import figure, output_file, show

output_file("grid_plot.html")

x = list(range(0,11))
y = list(range(10,21))

# cores
# orangered
# fucshia
# sea green

# colocando anotações no plot
span_annotation = Span(location = 13, dimension = "width", line_color = "DeepPink", line_width = 3)
box_annotation = BoxAnnotation(left = 3, right = 7, fill_color = "DeepPink")

plot1 = figure(width = 240, height = 240, title = "Circle Glyphs")
plot1.circle(x, y, size = 13, color = "OrangeRed", alpha = 0.42)

plot2 = figure(width = 240, height = 240, title = "Triangle Glyphs")
plot2.triangle(x, y, size = 13, color = "Fuchsia", alpha = 0.42)
plot2.add_layout(span_annotation)

plot3 = figure(width = 240, height = 240, title = "Circle Square")
plot3.square(x, y, size = 13, color = "SeaGreen", alpha = 0.42)
plot3.add_layout(box_annotation)

# organizando todos os plots numa grid
# a grid é interpretada como uma matriz feita por
# uma lista de listas
plot = gridplot([[plot1, plot2], [None, plot3]])

show(plot)
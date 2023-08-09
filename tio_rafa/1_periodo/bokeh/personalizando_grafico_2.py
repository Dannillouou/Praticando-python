from bokeh.plotting import figure
from bokeh.models import Range1d
from bokeh.io import output_file, save, show
from sklearn import datasets
import numpy as np

output_file("ainda_mais_bokeh.html")

plot = figure(width=640, height=480, 
              tools="box_zoom, pan, reset, save, wheel_zoom")# colocando todas as ferramentas que queremos

# exemplos ajustando a toolbar
# retirando símbolo que leva para o site do bokeh
plot.toolbar.logo = None
# mantém a barra de ferramentas escondida
plot.toolbar.autohide = True
# mudando localização da toolbar
plot.toolbar_location = "below"

renderer = plot.circle([1,2,3,4,5], [2,4,6,8,10], 
            legend_label="Sei la")# adicionando legenda à esse scatter plot

# ajustando legenda
plot.legend.location = "top"
plot.legend.location = "top_left"
plot.legend.background_fill_alpha = 0
plot.legend.border_line_color = "#ffbca4"
# plot.legend.border_radius = 5
plot.legend.label_text_color = "#ff99ff"
plot.legend.label_text_font = "times"
plot.legend.label_text_font_size = "45px"

# mudando renderizador dos pontos
glyph_renderer = renderer.glyph

# ajustando renderizador
glyph_renderer.size = 42
glyph_renderer.fill_alpha = 0.5
glyph_renderer.line_color = "#dfc76c"
glyph_renderer.line_width = 2
glyph_renderer.line_dash = [7,3]

show(plot)
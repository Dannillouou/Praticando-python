from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource 
# ColumnDataSource -> estrutura interna do bokeh que facilita muito a 
# compreensão do próprio bokeh. Dados podem ser convertidos de diversos
# formatos para o formato de ColumnDataSource, permitindo que diversos
# tipos de dados, como da web, por exemplo sejam usados na visualização

output_file("bokeh_ainda.html")

raw_data = {"x" : [1,2,3,4,5], "y" : [2,4,6,8,10]}

data_source = ColumnDataSource(data = raw_data)

plot = figure()
plot.circle(x = "x", y = "y", source = data_source)# source -> recebe o ColumnDataSource

new_data = [3,6,9,12,15]

data_source.data["extra"] = new_data
# data source funciona como funcionaria um dataframe no pandas
# novos nomes de colunas criam novas colunas

data_source.patch({ "x" : [(0,10)]})# alterando valor com índice 0 para 10

show(plot)
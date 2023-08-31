# if (__name__ == "__main__"):
# importando classe Flask
from flask import Flask

# esse atalho direciona para que o argumento busque o nome do projeto/pa
# ckage
app = Flask(__name__)

# então usamos o route para definir em qual url o flask deve ativar nossa
# função
@app.route("/")
# a função retorna o texto em formato HTML que será exibido no navegador 
# do cliente
def hello_world():
	return "<p> Hello, World!<p>"
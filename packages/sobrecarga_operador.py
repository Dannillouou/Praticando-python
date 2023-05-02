# Sobrecarga de operador (operator overloading)
# Quando um operadaor tem mais de uma funcionalidade, como o +
# que pode somar, concatenar, etc. ele tem uma sobrecarga de operador

# métodos começados e terminadas com "__" são 
# funções especiais (__init__, por exemplo) são usados pelo interpretador
# para implementar certas coisas. Algumas funções especiais do python:
# __init__() construtor do objeto
# __str__()	retorna uma representação em string do objeto
# __len__()	retorna a largura do objeto
# __add__()	"soma" dois objetos
# __call__() sama métodos da classe como uma função normal
# as funções especiais de sobrecarga de operador devem ser usadas dentro
# de uma mesma classe para comparar dois objetos baseados em algum atributo
# deles

class Ponto:
	x = 0
	y = 0
	def __init__(self, x = 0, y = 0) -> None: # o "-> None" indica que a função __init__ dessa classe não retorna nada
		self.x = x
		self.y = y
	
	def __str__(self) -> str: # "->" indica que o retorno da função é uma string
		return "{0}, {1}".format(self.x,self.y) # usando string como objeto
	
	def __add__(self, other):
		x = self.x + other.x
		y = self.y + other.y
		return Ponto(x, y)
	
ponto1 = Ponto(1,2)	
ponto2 = Ponto(3,3)

print(ponto1)
print(ponto2)
# quando usamos essa sintaxe python chama a função especial/mágica que soma os dois objetos
# que é o método __add__ definido no objeto
# se a função __add__ não for definida no objeto, o Python lança uma exceção "TypeError"
print(ponto1 + ponto2)
# é possível fazer todo tipo operação usando essa lógica de funções mágicas

# também é possível fazer a sobrecarga de operadores lógicos

class Pessoa:
	_idade = 0
	_nome = ""

	def __init__(self, idade = 0, nome = "fulano"):
		self._idade = idade
		self._nome = nome
	
	def __lt__(self, other):
		return self._idade < other._idade
	
# objetos pessoa
pessoa1 = Pessoa(45, "Carlos")
pessoa2 = Pessoa(15, "Mariana")

# comparando objetos pela idade, definido pelo método __lt__ dentro da classe
print(pessoa1 < pessoa2)


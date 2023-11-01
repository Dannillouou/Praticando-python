import os
import sys
project_root = os.path.dirname(os.path.dirname(__file__)) 
sys.path.append(project_root)

from utils.equals_line import equals_line


class Point2D():
	"""Classe que define um ponto no espaço bidimensional

	Attributes:
		x (int): posição no eixo x
		y (int): posição no eixo y
	"""

	def __init__(self, x, y) -> None:
		"""Construtor da classe Point2D

		Parameters
			x (int): posição no eixo x
			cdcdy (int): posição no eixo y
		"""
		self.x = x
		self.y = y
	
	def	set_x(self, value) -> None:
		if value < 0:
			print("Erro, o valor não pode ser menor que 0")
		else:
			self.x = value

	def	set_y(self, value) -> None:
		if value < 0:
			print("Erro, o valor não pode ser menor que 0")
		else:
			self.y = value



print(dir(Point2D)) # lista das propriedades internas inerentes à toda classe
equals_line()

point_1 = Point2D(10, 11)

# quando printamos um objeto, estamos sobrecrevendo o print para objetos
print(point_1)
equals_line()

print(type(point_1))
equals_line()

print(dir(point_1)) # aqui, além da lista inicial, surgem também x e y
equals_line()

point_1.x = 42 # forma incorreta
print(point_1.x) # 42
point_1.set_x(7) # forma correta
print(point_1.x) # 7
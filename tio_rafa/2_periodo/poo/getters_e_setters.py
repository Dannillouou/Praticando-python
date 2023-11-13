class Carro:
	# Propriedades ou atributos
	def __init__(self, marca, modelo) -> None:
		self.marca = marca
		self.modelo = modelo

	@property	
	def marca(self):
		print("Método get_marca foi invocado")
		return self._marca
	
	@marca.setter
	def marca(self, marca):
		print("Método set_marca foi invocado")
		self._marca = marca

	@property
	def modelo(self):
		print("Método get_modelo foi invocado")
		return self._modelo
	
	@modelo.setter
	def modelo(self, modelo):
		print("Método set_modelo foi invocado")
		self._modelo = modelo

	def descricao(self):
		return f"{self._marca}: {self._modelo}"


carro = Carro("Volvo", "XC40")

print(carro.marca)
print(carro.modelo)
print(carro.descricao())

carro.marca = "BMW"
carro.modelo = "X1"

print(carro.marca)
print(carro.modelo)

carro._marca = "Porsche"
print(carro.marca)
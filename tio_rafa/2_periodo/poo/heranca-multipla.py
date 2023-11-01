# Herança múltipla
class Classe_1:
	def ondestou(self):
		print("Na classe 1")

class Classe_2(Classe_1):
	def ondestou(self):
		print("Na classe 2")
		super().ondestou()

class Classe_3(Classe_1):
	def ondestou(self):
		print("Na classe 3")
		super().ondestou()

class Classe_4(Classe_3, Classe_2):
	def ondestou(self):
		print("Na classe 4")
		super().ondestou()

obj_1 = Classe_4()
obj_1.ondestou()

# O Method Resolution order é o algoritmo que decide onde procurar por
# um determinado método quando este não for encontrado na classe em
# questão.
print(Classe_4.mro())
print(Classe_4.__mro__)
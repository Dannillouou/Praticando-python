class Fruta:
	def __init__(self, nome):
		print("fruta criada")
		self.nome = nome

	def comer(self):
		print(f"A fruta {self.nome} está sendo comida!")

banana = Fruta("Banana")		
banana.comer()
print("\n")


manga = Fruta("Manga")		
manga.__init__("Nao eh manga")
print("\n")

Fruta.comer(
	Fruta("Pera")
)


uva = Fruta("Uva")
print(vars(uva))
print(uva.__dict__)
print("\n")

uva.peso = 1
uva.data = "31/10/2023"
print(vars(uva))
del uva.__dict__["peso"]
print(uva.__dict__)
# herança multipla:
# quando uma classe é filha de mais de uma classe ao mesmo tempo

# classes mae
class Mamifero:
    def mamifero(self):
        print("mamiferos dao a luz")

    def animal(self):
        print("sou um animal e sou mamifero")


class BichoVoador:
    def voa(self):
        print("voa")
    
    def animal(self):
        print("sou um animal e voo")


# classe herdando todos os metodos das suas superclasses
class Morcego(Mamifero, BichoVoador):
    __nome = ""

    def __init__(self, nome):
        self.__nome = nome

    def morcego(self):
        print("rato c asa")

    def dizNome(self):
        print(self.__nome)


murcego = Morcego("batimao")
murcego.mamifero()
murcego.voa()
murcego.dizNome()
# usando metodo definido nas duas classes maes
# o MRO (Method Resolution Order) define que a classe definida 
# primeira tem preferência
murcego.animal()

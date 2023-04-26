# # classe poligono
# class Poligono:
#     def __init__(self, num_lados):
#         self.__num_lados = num_lados
#         # este codigo esta errado
#         self.lados = [0 for i in range(num_lados)]

#     def inputLados():
#         self.lados = [float(input("insira o lado" + str(i + 1) + " : " for i in range(self.__num_lados)))]

#     def mostra_lados():
#         for i in range(self.__num_lados):
#             print("Side ", i+1, "is ", self.lados[i])

# class Triangulo(Poligono):
#     # sobrescrevendo construtor
#     def __init__(self, num_lados):
#         super().__init__(num_lados)
    
#     def calcularArea():
#         a, b, c = self.lados
#         # pelos tres lados
#         s = (a + b + c)
#         area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
#         print('A area do triangulo é: %0.2f', area)

class  Animal:
    __nome = ""
    
    def __init__(self,nome):
        self.__nome = nome

    def comer(self):
        print("Eu posso comer")

    def dizNome(self):
        print("Meu nome é:", self.__nome)

# criando classe filha
class Cachorro(Animal):
    __raca = ""
    
    # escrevendo sobre o construtor aproveitando o que ele já tinha
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.__raca = raca

    # aproveitando o que já tinhamos no método novamente
    def comer(self):
        super().comer()

        print("Eu gosto de comer carne")

labrador = Cachorro("doguinho", "labrador")

labrador.dizNome()
# por ser um objeto do tipo cachorro, comer printa o que tem na classe
# Animal e na classe Cachorro
labrador.comer()

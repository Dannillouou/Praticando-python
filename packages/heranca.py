# classe de erro
class TrianguloNaoExiste(Exception):
    def __init__(self, mensagem="os lados recebidos não satisfazem as condições de existência"):
        self.mensagem = mensagem
        super().__init__(self.mensagem)

# classe poligono
class Poligono:
    def __init__(self, num_lados):
        self.__num_lados = num_lados
        self.lados = []

    def inputLados(self):
        # self.lados = [float(input("insira o lado" + str(i + 1) + " : " for i in range(self.__num_lados)))]
        # não é feita verificação de se o polígono é válido
        for i in range(self.__num_lados):
            self.lados.append(int(input(f"Digite o {i + 1} lado do poligono: ")))

    def mostra_lados(self):
        for i in range(self.__num_lados):
            print("Lado ", i + 1, "é: ", self.lados[i])

class Triangulo(Poligono):
    # sobrescrevendo construtor
    # não tenho certeza se esse num lados igual a 3 pode ficar assim mas por hora vai ser
    def __init__(self, num_lados = 3):
        super().__init__(num_lados)

    def inputLados(self):
        super().inputLados()
        # avaliação de se o triângulo pode existir ou não
        if (self.lados[0] < self.lados[1] + self.lados[2]) and (self.lados[0] > self.lados[1] - self.lados[2]):
            if (self.lados[1] < self.lados[0] + self.lados[2]) and (self.lados[1] > self.lados[0] - self.lados[2]):
                if (self.lados[2] < self.lados[0] + self.lados[1]) and (self.lados[2] > self.lados[0] - self.lados[1]):
                    raise TrianguloNaoExiste()

    def calcularArea(self):
        a, b, c = self.lados
        # pelos tres lados
        s = (a + b + c)
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('A area do triangulo é: %0.2f', area)

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

triangulo = Triangulo()
triangulo.inputLados()
print(triangulo)
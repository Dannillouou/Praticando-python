# classe mae
# a palavra chave self é chamada dentro de todo e qualquer método dentro de uma classe
# pelo que entendi até agora

# atributos privados
# quando colocamos o "__" para definir um atributo, o python na verdade faz uma
# organização interna dos atributos, fazendo uma separação entre o atributo de uma
# classe superior e uma inferior para não ocorrer problemas
# A convenção é de usar "_" para dizer que o atributo não deve ser acessado fora
# da classe. Se for uma preocupação os nomes conflitarem, deve ser colocado o nome
# da classe na frente do atributo


# ==================herança=======================

class  Animal:
    # essa forma de proteger o atributo é uma convenção. O "_" não significa
    # nada para o python, por isso colocamos também a classe antes, mas é uma
    # convenção de que esse atributo não deve ser acessados fora da classe
    _nome = ""
    
    def __init__(self,nome):
        self._nome = nome

    def comer(self):
        print("Eu posso comer")

    def dizNome(self):
        print("Meu nome é:", self._nome)

# criando classe filha
class Cachorro(Animal):
    _raca = ""
    
    # escrevendo sobre o construtor aproveitando o que ele já tinha
    def __init__(self, nome, raca):
        super().__init__(nome)
        self._raca = raca

    # aproveitando o que já tinhamos no método novamente
    def comer(self):
        super().comer()

        print("Eu gosto de comer carne")

labrador = Cachorro("doguinho", "labrador")

labrador.dizNome()
# por ser um objeto do tipo cachorro, comer printa o que tem na classe
# Animal e na classe Cachorro
labrador.comer()

# ==================herança e exceções=======================
# classe de erro
class TrianguloNaoExiste(Exception):
    def __init__(self, mensagem="os lados recebidos não satisfazem as condições de existência"):
        self.mensagem = mensagem
        super().__init__(self.mensagem)

# classe poligono
class Poligono:
    def __init__(self, num_lados):
        self._num_lados = num_lados
        self.lados = []

    def inputLados(self):
        # self.lados = [float(input("insira o lado" + str(i + 1) + " : " for i in range(self._num_lados)))]
        # não é feita verificação de se o polígono é válido
        for i in range(self._num_lados):
            self.lados.append(int(input(f"Digite o {i + 1} lado do poligono: ")))

    def mostra_lados(self):
        for i in range(self._num_lados):
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


# ==================herança múltipla=======================

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
    _nome = ""

    def __init__(self, nome):
        self._nome = nome

    def morcego(self):
        print("rato c asa")

    def dizNome(self):
        print(self._nome)


murcego = Morcego("batimao")
murcego.mamifero()
murcego.voa()
murcego.dizNome()
# usando metodo definido nas duas classes maes
# o MRO (Method Resolution Order) define que a classe definida 
# primeira tem preferência
murcego.animal()


# ==================polimorfismo=======================

# polimorfismo
class Poligono:
    # gerar um formato
    def gerar(self):
        print("gerando poligono...")


class Quadrado(Poligono):
    # gerar quadrado
    def gerar(self):
        print("gerando quadrado...")


class Circulo(Poligono):
    # gerar circulo
    def gerar(self):
        print("gerando circulo...")


# criando objeto de Quadrado
quadrado = Quadrado()
quadrado.gerar()

# criando objeto de Circulo
circulo = Circulo()
circulo.gerar()

# o mesmo método gerar existe de várias formas diferentes para duas subclasses
# de uma mesma superclasse, isso é o polimorfismo


# ==================sobrecarga de operador=======================

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


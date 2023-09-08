# a função property permite que tenhamos atributos praticamente
# privados em python, pois cria uma interface em que de qualquer forma
# a propriedade é manipulada por métodos e ainda permite que haja uma espécie
# de retro compatibilidade com "versões mais antigas" da classe


# classe que armazena temperatura em celsius e converte para Fahrenheit
"""
class Celsius:
    def __init__(self,temperatura = 0) -> None:
        self.temperatura = temperatura

    def converte_fahrenheit(self):
        return (self.temperatura * 1.8) + 32
    
# forma básica de manipular atributos em objetos
# criando objeto
temperatura_humano = Celsius()

# setando temperatura
temperatura_humano.temperatura = 37

# pegando (get) a temperatura
print(temperatura_humano.temperatura)

# pegando o valor em fahrenheit
print("%.2f" % temperatura_humano.converte_fahrenheit())

print(temperatura_humano.__dict__)
"""

# refazendo objeto
"""
class Celsius:
    def __init__(self, temperatura = 0) -> None:
        self.set_temperatura(temperatura)

    def converter_para_fahrenheit(self):
        return (self.get_temperatura() * 1.8) + 32
    
    # método getter
    def get_temperatura(self) -> float:
        return self._temperatura
    
    # método setter
    def set_temperatura(self, valor) -> None:
        if valor < -273.15:
            raise ValueError("A temperatura de um objeto não pode ser menor do que -273.15 graus Celsius")
        self._temperatura = valor

# cria um novo objeto e set_temperatura chamado pelo construtor
temperatura_humano = Celsius(37)

# get a temperatura
print(temperatura_humano.get_temperatura())

# pegando a temperatura em fahrenheit
print(temperatura_humano.converter_para_fahrenheit())
"""

# levantando erros
# temperatura_humano.set_temperatura(-300) # levanta erro

#================================================================
# se tívessemos que implementar essas alterações nas versões
# antigas da classe, seria um trabalho muito grande em projetos
# muito grandes 

# como lidamos com o problema? @property

# terceira versão da classe 
"""
class Celsius:
    def __init__(self, temperatura = 0) -> None:
        self.temperatura = temperatura

    def converter_para_fahrenheit(self):
        return (self.get_temperatura() * 1.8) + 32
    
    # método getter
    def get_temperatura(self) -> float:
        print("obtendo valor...")
        return self._temperatura
    
    # método setter
    def set_temperatura(self, valor) -> None:
        print("mudando valor...")
        if valor < -273.15:
            raise ValueError("A temperatura de um objeto não pode ser menor do que -273.15 graus Celsius")
        self._temperatura = valor

    # usando o decorador interno property que seta os métodos criados por nós como métodos
    # getter e setter para o objeto
    temperatura = property(get_temperatura, set_temperatura)
    # o valor fica da temperatura fica armazenado numa variável privada _temperatura
    # e o atributo temperatura funciona só como uma interface para isso

# a criação do objeto chama o método setter mesmo que esse não esteja 
# implementado no construtor graças ao decorardor property
temperatura_humana = Celsius(37)
print(temperatura_humana.get_temperatura())
temperatura_humana.set_temperatura(45)
print(temperatura_humana.get_temperatura())
# mesmo tentando mudar diretamente o setter é chamado
# no objeto
temperatura_humana.temperatura = 50
print(temperatura_humana.get_temperatura())
# temperatura_humana.temperatura = -300 #esse comando da erro
print(temperatura_humana.get_temperatura())
"""

# a função property cria um objeto property que funciona 
# como uma espécie de interface
# funciona como se fosse um decorador pois o atributo
# temperatura se torna uma função que implementa o método
# getter/setter criado manualmente para atualizar o atributo
# privado temperatura
# contudo, ainda é possível acessar diretamente o atributo privado
# python = paia
class Celsius:
    def __init__(self, temperatura) -> None:
        self.temperatura = temperatura

    def converte_fahrenheit(self):
        return(self.temperatura * 1.8) + 32
    
    @property
    def temperatura(self) -> float:
        print("pegando valor...")
        return self._temperatura

    @temperatura.setter
    def temperatura(self, valor):
        print("mudando valor...")
        if valor < -273.15:
            raise ValueError("A temperautra não pode ser menor que -273.15 graus Celsius")
        self._temperatura = valor

temperatura_humana = Celsius(37)
print(temperatura_humana.temperatura)
# aparentemente mudando diretamente mas chamando setter
temperatura_humana.temperatura = 45 # printa "mudando valor..."
print(temperatura_humana.temperatura)
# tentando manipular o atributo privado
temperatura_humana._temperatura = -300 # aparentemente funciona
print(temperatura_humana._temperatura) # não levanta ValueError
print(temperatura_humana.temperatura) #python sendo python
#levantando erro
# temperatura_humana.temperatura = -300
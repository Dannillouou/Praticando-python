# # classe que armazena temperatura em celsius e converte para Fahrenheit
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
class Celsius:
    pass

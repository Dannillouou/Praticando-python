# modulo para usar operações com strings em python
import string

# modulo que 

alfabeto = list(string.ascii_uppercase)

# objeto iterador
# cria um objeto iterável para percorrermos
# a função chamada só com o primeiro argumento necessita de um objeto
# que aceita o protocolo de iteração (__iter__) o que possa ser percorrido
# com índices inteiros, como uma lista
iterador = iter(alfabeto)

# iterando através do objeto iterador
print(str(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
# se tentarmos pegar um proximo elemento depois do objeto já ter
# terminado, o python lança uma exceção (explode) "StopIteration"

# usando o for com um objeto iterador, a função de loop o percorre
# até a exasutão (não haver mais como percorrer)
for elemento in iterador:
    print(elemento)

# isso lança a exceção:
# print(next(iterador))

# iterador personalizado
class PotenciaDois:
    # implementar um iterador de potências de dois
    
    contador = 0
    
    def __init__(self, max = 0) -> None:
        self.max = max
    
    def __iter__(self):
        self.contador = 0
        return self
    
    def __next__(self):
        # se ainda não tiver chegado no fim, retorna a potência
        # de dois do proximo elemento do iterador
        if self.contador <= self.max:
            resultado = 2 ** self.contador
            self.contador += 1
            return resultado
        else:
            raise StopIteration
        
exponencial_dois = PotenciaDois(10)

for potencia in exponencial_dois:
    print(potencia)


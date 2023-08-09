# gerador é uma função que retorna um iterador
# que produz uma sequência de valores para iterarmos
# sorbe. Geradores são úteis quando queremos uma grande
# sequência de valores mas não queremos armazenar
# todos na memória ao mesmo tempo

def gerador(n):

    # inicilizando contador
    valor = 0

    # loop enquanto o contador for menor que n
    while valor < n:

        # a palavra chave dos geradores é "yield", que produz o valor
        # do gerador. Yield significa colheira, que é como a função re
        # tornar o valor sem ser finalizada
        yield valor

        valor += 1
    

# na prática esse gerador funciona como o range()
# o for itera sobre o objeto gerado pela função geradora
for valor in gerador(100):
    print(valor) # printa de 1 a 99

# podemos também criar um objeto iterador com a função geradora
gerado = gerador(10)
print(next(gerado)) # printa 0
print(next(gerado)) # printa 1

# gerador de potencias em uma linha
gerador_potencia = (num * num for num in range(20))

print("Dentro do for:")
for valor in gerador_potencia:
    print(valor) # printa de 0 a 19^2

# definindo a mesma ideia da classe iteradora de potencias de dois, 
# mas com gerador

# 
def Exponencial(base = 2, expoente_maximo = 0):
    expoente = 0
    while expoente < expoente_maximo:
        yield base ** expoente
        expoente += 1

funcao_exponencial = Exponencial(3, 10)

for valor in funcao_exponencial:
    print(valor)

# funções geradoras são mais eficientes na memória, pois
# são um iterável que entrega um número de cada vez, sem precisar
# 
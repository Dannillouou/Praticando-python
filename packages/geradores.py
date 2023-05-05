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

print("Dentro do for:")
for valor in gerado:
    print(valor) # printa de 2 a 9
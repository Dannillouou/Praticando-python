import random as rand

#criando lista vazia
aleatorios = []

#colocando numeros aleatorios
for i in range(50):
    aleatorios.append(rand.randrange(1,51))

print(aleatorios)

#avaliando qual o maior e o menor
for numero in range(0, len(aleatorios)):
    if numero == 0:
        maior = aleatorios[numero]
        menor = aleatorios[numero]
    else:
        if numero > maior:
            maior = aleatorios[numero]
        elif numero < menor:
            menor = aleatorios[numero]

print(f"maior numero: {maior}, menor numero: {menor}")
import random as rand

#criando lista vazia
aleatorios = []

#colocando numeros aleatorios
for i in range(50):
    aleatorios.append(rand.randrange(1,51))

print(aleatorios)

#ordenando
aleatorios.sort()
print(aleatorios)
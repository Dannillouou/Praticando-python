quant_numeros = int(input())
lista_numeros = []
for i in range(quant_numeros):
    numero = int(input())
    if numero != 0:
        lista_numeros.append(numero)
    else:
        lista_numeros.pop()

total = 0

for numero in lista_numeros:
    total += numero

print(numero)
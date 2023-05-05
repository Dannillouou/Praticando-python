continuar = True

numeros = []
soma = 0
while continuar:
    num = float(input("gimme a number"))
    soma += num
    numeros.append(num)
    decisao = input("queres parar? [S/N]")
    if decisao == 'S':
        continuar = False

print("A soma de ")
for numero in numeros:
    if(numero == num):
        print(numero, "= ", end="")    
    else:
        print(numero, "+ ", end="")

print(soma)
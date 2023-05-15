print("Programa que calcula o valor de H = 1 + 1/2 + 1/3 ... 1/N\n\n")

denominador_maximo = int(input("digite o valor de n: "))

print("H = ", end="")
soma = 0
for i in range(1, denominador_maximo + 1):
    soma += 1/i
    if i != denominador_maximo:
        print(f"1/{i} + ", end="")
    else:
        print(f"1/{i}", end="")

print(f"\n= {soma}")
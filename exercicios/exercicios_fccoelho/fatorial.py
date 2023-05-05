num = int(input("gimme number: "))

resultado = 1
for i in range(num, 0, -1):
    resultado *= i

print(resultado)
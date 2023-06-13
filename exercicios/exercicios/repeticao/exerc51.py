def gerador_numeros_da_sequencia(valor_maximo_n):
	n = 1
	m = 1

	while n <= valor_maximo_n:
		yield tuple([n,m])
		n += 1
		m += 2

print("O programa calcula o valor de S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m")

valor_maximo_n = int(input("Digite o valor de n: "))

print("S = ", end="")
soma = 0
for tupla in gerador_numeros_da_sequencia(valor_maximo_n):
	n, m = tupla
	soma += n/m
	if n != valor_maximo_n:
		print(f"{n}/{m} + ", end="")
	else:
		print(f"{n}/{m}")

print(f"= {soma}")
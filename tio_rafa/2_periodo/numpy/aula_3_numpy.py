import math
import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt

# Discutindo propriedades de numpy

# No numpy, a biblioteca math é implementada de forma muito eficiente junto dos vetores
#============================================================================
print("Broadcasting")

# Broadcasting:
# A operação feita no vetor é aplicada separadamente em cada elemento do vetor

lista_a = [1, 2 ,3]
lista_b = [4, 5 ,6]

array_1d_a = np.array([1, 2, 3, 4])
array_1d_b = np.array([0, 1, 2, 3])

# Operações Básicas
# print(lista_a * lista_b)
# ERRO: não é possível multiplicar sequencia por não-inteiro

# Multiplicação
print(array_1d_a * array_1d_b)

print(lista_a * 3) # concatena 3 listas
print(array_1d_a * 3) # multiplica tudo por 3

# Soma
# print(lista_a + 3)
# ERRO: Não pode concatenar um inteiro na lista

print(array_1d_a + 3) # adiciona 3 em tudo

# Subtração
# print(lista_a - 3)
# ERRO: operando não supertado para listas e inteiros

print(array_1d_a - 3) # subtrai 3 de tudo

# Exponenciação
# print(lista_a ** 3)
# ERRO: Operando ** nao suportado para listas e inteiros

print(array_1d_a ** 3) # eleva tudo a 3

#Divisão
# print(lista_a / 3)
# ERRO: Operando / nao suportado para listas e inteiros

# print(array_1d_a / 3) # dividde tudo por 3
print(array_1d_a / 0) # trata divisão por 0 como infinito
print(array_1d_b / 0) # 0/0 se torna nan(not a number)

print("\n\n")

#============================================================================
# Produtos entre NDArrays
print("Produtos entre arrays")

array_1d_a = array_1d_a.reshape(1,4)
array_1d_b = array_1d_b.reshape(4,1)

print(array_1d_a * array_1d_b)

print("\n\n")

#============================================================================
# BAGULHO DOIDO
# Podemos filtrar um array, que gera uma estrutura de dados com verdadeiros e falsos
# que pode ser usada no indexamento de arrys para selecionar os elementos que atendem
# às condições

print("BAGULHO DOIDO")

ndarray = np.array([1,2,3,4,5,6])

indices = ndarray>3
print(indices) # [False False False  True  True  True]
print(ndarray[indices]) # [4 5 6]

indices = (ndarray%2 == 0)
print(indices) # [False  True False  True False  True]
print(ndarray[indices]) # [2 4 6]

print("\n\n")

#============================================================================
ndarray = np.arange(9).reshape(3,3) # array de 0 até 8 em 3x3
indices = np.array([[False, True, False],[True, False, True], [True, True, True]]) # matriz 3x3 de verdadeiros e falsos
print(ndarray)
print(indices)

print(ndarray[indices]) # seleciona apenas os índices com True

print("\n\n")

#============================================================================
# Operações estatísticas

# notas de Breaking Bad
notas = np.array([87, 72, 95, 93, 70, 100])

# Average
print("Average: ", np.average(notas))

# Median
print("Median: ", np.median(notas))

# Standart Deviation
print("Standart Deviation: ", np.std(notas))

# Minimun e Maximun
print("Mínimo: ", np.amin(notas),"e Máximo: ", np.amax(notas))

# Percentile
print("Percentile [70]: ", np.percentile(notas,70))

# Peak to Peak
print("Peak to Peak: ", np.ptp(notas))

#============================================================================
"""
Exercício:
Elaborar um programa que trata de uma matriz 2xn composta por:

1 - Uma coleção de valores estimados
2 - Uma coleção de valores observados

Elaborem 4 funções:

1 - Exibir o erro médio absoluto
2 - Exibir o erro médio quadrático
3 - Exibir os dados gerais da coleção (Estatísticos)
4 - Exibir o histograma da coleção

"""

colunas = npr.randint(low = 1, high = 20)
array_estimados = npr.random_sample((colunas,))
array_observados = npr.random_sample((colunas,))
matriz_exercicio = np.array([array_estimados, array_observados])
print(matriz_exercicio)

# erro médio absoluto
def erro_medio_absoluto(matriz):
    mae_matriz = np.mean(matriz_exercicio[0] - matriz_exercicio[1])
    print(mae_matriz)

# erro médio quadrático
def erro_medio_quadratico(matriz):
    eqm_matriz = np.mean((matriz_exercicio[0] - matriz_exercicio[1]) ** 2)
    print(eqm_matriz)

# estatísticas
# Average
print("Média estimados: ", np.average(matriz_exercicio[0]))
print("Média observados: ", np.average(matriz_exercicio[1]))

# Median
print("Mediana estimados: ", np.median(matriz_exercicio[0]))
print("Mediana observados: ", np.median(matriz_exercicio[1]))

# Standart Deviation
print("Desvio padrão estimados: ", np.std(matriz_exercicio[0]))
print("Desvio padrão observados: ", np.std(matriz_exercicio[1]))

# Minimun e Maximun
print("Mínimo e máximo estimados: ", np.amin(matriz_exercicio[0]), np.amax(matriz_exercicio[0]))
print("Mínimo e máximo observados: ", np.amin(matriz_exercicio[1]), np.amax(matriz_exercicio[1]))

# Percentile
print("Percentil [50] estimados: ", np.percentile(matriz_exercicio[0],50))
print("Percentil [50] observados: ", np.percentile(matriz_exercicio[1],50))

# Peak to Peak
print("Peak to peak estimados: ", np.ptp(matriz_exercicio[0]))
print("Peak to peak observados: ", np.ptp(matriz_exercicio[1]))

# Histograma
hist_estimados = np.histogram(matriz_exercicio[0], bins = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
hist_observados = np.histogram(matriz_exercicio[0], bins = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])

print("Histograma valores estimados: ", hist_estimados)
print("Histograma valores observados: ", hist_observados)

plt.hist(x = matriz_exercicio[0])
plt.show()
plt.hist(x = matriz_exercicio[1])
plt.show()
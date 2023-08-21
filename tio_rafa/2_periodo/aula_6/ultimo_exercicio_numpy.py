import numpy as np
import numpy.random as npr
import math

# Encontrar os valores comuns entre dois vetores

array_1 = npr.randint(100, size = 100)
array_2 = npr.randint(100, size = 100)

print(np.intersect1d(array_1, array_2))

# Em um vetor com 100 elementos (0-99), inverta os valores de 
# 42 até 66

array_3 = np.arange(100)
array_3[(array_3>41) & (array_3<67)] *= -1
print(array_3)

# Encontre o elemento de um vetor mais próximo de um dado valor
valor = 50
array_4 = npr.randint(100, size = 100)

# vetor que guarda a menor diferença registrada e o indice relacionada a ela
# Minha versão
indice_mais_proximo = np.array([100, 0])

for i in range(array_4.size):
    if (int(math.sqrt((valor - array_4[i])**2)) < indice_mais_proximo[0]):
    # aqui foi feita a operação de valor absoluto na diferença entre o valor atual
    # e o valor procurado e feita a comparação da distancia do valor atual no array 
    # com a última menor distancia registrada no array indice mais proximo, que 
    # armazena essa distancia na primeira posição e o indice do numero relacionado 
    # a ela na segunda posição
        print("Distancia absoluta ", int(math.sqrt((valor - array_4[i])**2)), " indice: ", i)
        indice_mais_proximo[0] = int(math.sqrt((valor - array_4[i])**2))
        indice_mais_proximo[1] = i

print(array_4)
print("Indice do valor mais proximo de ", valor, ": ", indice_mais_proximo[1], sep="")

# Versão do professor
array_4 = np.arange(10)
valor = npr.uniform(0,10)

indice_elemento = (np.abs(array_1-valor)).argmin()
print(valor)
print(indice_elemento, array_1[indice_elemento])
import numpy as np

print(np.__version__)

# criando arrays
lista_1 = list(range(1,5))
lista_2 = list(range(5,9))
array_1 = np.array(lista_1)
array_2 = np.array(lista_2)

print(array_1)
print(array_2)

# concatenando arrays 
array_concat = np.concatenate((array_1, array_2)) # a função recebe uma tupla

print("Array concatenado: ", array_concat)

# como string
print("Pritando como string: ", array_concat.astype(str))

# informações do array
print(f"Dados sobre array_1:\nDimensao: {array_1.ndim}\nTamanho: {array_1.size}\nTipo: {array_1.dtype} \nTamanho do elemento: {array_1.itemsize}")

# array bidimensional
array_2D = np.array([lista_1, lista_2])

print(array_2D)
# informações do array bidimensional
print(f"Dados sobre array_2D:\nDimensao: {array_2D.ndim}\nTamanho: {array_2D.size}\nTipo: {array_2D.dtype} \nTamanho do elemento: {array_2D.itemsize}")

# percorrendo array
print("Percorrendo array_2D: ", array_2D[0, 3])# 4

# slice 
print("Percorrendo array concatenado: ", array_concat[2:6:2])# [3 5]

# slice bidimensional
print("Percorrendo array_2D: ", array_2D[::-1,::-1])# o primeiro organiza as linhas e o segundo as colunas

# shape/fornma
print(f"forma do array_2D: {array_2D.shape}")

# 3D
lista_3 = list(range(9, 13))
lista_4 = list(range(10, 17))

# lista de listas de listas
array_3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(array_3D)
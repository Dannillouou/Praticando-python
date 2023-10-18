import numpy as np
import numpy.random as npr

# Operações NDArrays
print("#"*40)

array1D = np.arange(10)
print(array1D, end="\n" + "#"*40 + "\n")# quebrar linha e adicionar 40 hashtags

array1D = array1D.reshape(5,2)
print(array1D, end="\n" + "#"*40 + "\n")

try:
    array1D = array1D.reshape(3,2)
except ValueError:
    print("Não é possível fazer essa conversão!")

array1D = array1D.transpose()

print(array1D, end="\n" + "#"*40 + "\n")

array2D = np.arange(20)

try:
    array2D = array2D.reshape(10,2)
except ValueError:
    print("Não é possível fazer essa conversão!")

print(array2D, end="\n" + "#"*40 + "\n")

array3D = np.vstack((array2D,array2D))   
print(array3D, end="\n\n")

array3D = np.hstack((array2D,array2D))
print(array3D, end="\n\n")


print(f"Dados sobre array3D:\n\tDimensão: {array3D.size}\n\tForma: {array3D.shape}")

'''
#Shallow copy
array1D_copy = array1D
array1D_copy[0] = 42

print(id(array1D))
print(id(array1D_copy))
#mesmo id

#Deep copy
array1D_copy = array1D.copy()
array1D_copy[0] = 42

print(id(array1D))
print(id(array1D_copy))
#id muda
'''

outro_vetor = array1D.reshape(5,2)
outro_vetor[0,0] = 42

print(array1D)
print(outro_vetor)

print(id(array1D))
print(id(outro_vetor))
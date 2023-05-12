#numpy permite ter uma forma de trabalhar com lista como se fossem matrizes

import numpy as np

a = np.array([1, 2, 3, 4, 5,6])

print(a) # printa a matriz
print(a.shape) # printa o que seria o shape da matriz ou o tamanho de certa forma

a.shape = (2,3) # isso é bagunça

print(a.shape)

# forma correta
# a.reshape()
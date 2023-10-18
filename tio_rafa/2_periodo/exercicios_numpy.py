import numpy as np
import numpy.random as npr

exercicio_1 = np.zeros((1,42))
print(exercicio_1)

exercicio_2 = np.ones((1,42))
print(exercicio_2)

exercicio_3 = np.identity(5)
print(exercicio_3)

exercicio_4 = np.array(list(range(7,43)))
print(exercicio_4)

exercicio_5 = np.array(list(range(8,43,2)))
print(exercicio_5)

exercicio_6 = npr.uniform(0,1)
print(exercicio_6)

exercicio_7 = npr.normal(size=(1, 10))
print(exercicio_7)

exercicio_8 = np.arange(10)
for i in range(exercicio_8.size):
    exercicio_8[i] = 42
print(exercicio_8)

exercicio_9 = np.arange(1,10)
exercicio_9 = exercicio_9.reshape(3,3)
print(exercicio_9)


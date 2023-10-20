import numpy as np
import time

# vetorização de função

# usando a função time do modulo time para pegar o momento atual
inicio_tempo_vetorizacao = time.time()

vetor_loop = np.array(range(1,10000000))

for number in range(len(vetor_loop)):
    vetor_loop[number] = vetor_loop[number] ** 2

fim_tempo_vetorizacao = time.time()

print("Tempo de loop: ", fim_tempo_vetorizacao - inicio_tempo_vetorizacao)
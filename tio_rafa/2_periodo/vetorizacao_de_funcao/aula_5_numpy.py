import numpy as np
import time

# vetorização de função

# usando a função time do modulo time para pegar o momento atual
inicio_tempo_loop = time.time()

vetor_loop = list(range(1,11))

for number in range(len(vetor_loop)):
    vetor_loop[number] = vetor_loop[number] ** 2

fim_tempo_loop = time.time()

print("Tempo de loop: ", fim_tempo_loop - inicio_tempo_loop)

# qual o indice do 10 elemento em uma matriz 5x5
print(np.unravel_index(10, (5,5)))

# qual o indice do 42 elemento em uma maitrz 5x5x5
print(np.unravel_index(42, (5,5,5)))

# xadrez
chess_board = np.zeros((8,8))
chess_board[1::2,::2] = 1
chess_board[::2,1::2] = 1

print(chess_board)

from utils import swap

# Heapify.
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    # Se o filho da esquerda existir e for maior que a raíz.
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Se a raíz não for mais o valor inicial.
    if largest != i:
        swap(arr, largest, i)
        heapify(arr, n, largest)
        
# Build Heap
# Pega vetor e faz pra cada posição a verificação (começando do nó com um filho):
# Se o pai for menor que o filho, executa o heapify para corrigir aquela subárvore.
def buildHeap(arr, n):
    # Percorrendo vetor de trás pra frente
    for idx in range(n // 2 - 1, -1, -1):
        heapify(arr, n, idx)

def heapSort(arr):
    n = len(arr)
    buildHeap(arr, n)

    for idx in range(n - 1, -1, -1):
        swap(arr, 0, idx)
        heapify(arr, idx, 0)

if __name__ == "__main__":
    import numpy as np
    
    arr = np.random.randint(100, size=20)
    arr = list(arr.tolist())
    print(arr)
    heapSort(arr)
    print(arr)
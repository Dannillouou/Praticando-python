# import numpy as np
# np.random.seed(42)

# Lista de exemplo.
# arr = np.random.randint(100, size=10)
# arr = list(arr.tolist())
# print(arr)

from utils import swap

arr = [
    8,
    11,
    2,
    5,
    1,
    16,
    4,
    15,
    9,
    7,
]

# Algoritmo de N. Model.
# Escolhemos o úlitmo elemento.
# Colocamos j como o primeiro.
# Percorremos o vetor com i. Se i for menor que x, trocamos tudo entre i e j e j + 1.
# Ao final colocamos o pivõ na sua posição correta (j).

def partition(arr, p ,r):
    """
    Auxiliary function that partitionates the array.
    """
    
    # Setting last element as the pivot.
    x = arr[r]
    j = p

    # Traversing the array moving elements less then the pivot o the left and
    # greater than the pivot to the of where to pivot should be.
    for idx in range(p, r):
        if arr[idx] <= x:
            swap(arr, j, idx)
            
            j += 1

    swap(arr, j, r)
    # Putting the pivot in its right position.
    return j

# Quicksort
# Particiona a sequência.
# Executa recursivamente nas partições ao redor do pivô.
# Ordena partições menores (1 ou 2 elementos)

def quickSort(arr, p, r):
    print(arr)

    if p < r:
        j = partition(arr, p, r)
        quickSort(arr, p, j - 1)
        quickSort(arr, j + 1, r)
    
    return arr

print(quickSort(arr, 0, len(arr) - 1))

# void quicksort(int v[], int p, int r) {
#     while (p < r) {
#         int j = partition(v, p, r);
#         if (j - p < r - j) {
#             quicksort(v, p, j - 1);
#             p = j + 1;
#         } else {
#             quicksort(v, j + 1, r);
#             r = j - 1;
#         }
#     }
# }


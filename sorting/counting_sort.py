def countingSort(arr, n):
    # Descobrir maior elemento.
    greatest = arr[0]
    for idx in range(1, n):
        if arr[idx] > greatest:
            greatest = arr[idx]

    # Vetor com tamanho dele.
    fs = list(range(greatest + 2))
    # Colocar todas as posições como 0
    for idx in range(len(fs)):
        fs[idx] = 0

    # Contar a ocorrência de cada elemento e colocar nesse vetor (uma posição pra frente,
    # ou seja, se acharmos um 1 colocamos 1 a mais para o 2)
    for idx in range(n):
        fs[arr[idx] + 1] += 1

    # Contar a frequência acumulada para cada posição no vetor.
    for idx in range(1, len(fs)):
        fs[idx] += fs[idx - 1]

    # Ordenar vetor final:
    # Criamos um vetor temporário que vai armazenar a sequência ordenada.
    temp = list(range(n))

    # Percorremos o vetor inicial e para cada posição i.
    for idx in range(n):
        # Colocamos i numa variável.
        j = arr[idx]
        # Colocamos no vetor temporário o i na posição correta (baseada na 
        # contagem de elementos antes do i em fs).
        temp[fs[j]] = j
        # Aumentamos a contagem em fs para o próximo elemento igual a v[i]
        fs[j] += 1

    # Por fim, colocamos o vetor temporário no vetor final ordenado.
    for idx in range(n):
        arr[idx] = temp[idx]

if __name__ == "__main__":
    import numpy as np
    
    arr = np.random.randint(6, size=1000000)
    print(arr)

    n = len(arr)
    countingSort(arr, n)
    
    print(arr)
def rodandoRepeticao():
    # Estruturas de repetição
    # usando else if
    number = 0
    alfabeto = ["A", "B", "C", "D"]

    if number > 0:
        print("Positive number")

    elif number == 0:
        print('Zero')
    else:
        print('Negative number')

    # usando emoji
    print('Pyhton usa elif mano que trem feio \U0001F922')

    # Usando for
    # Iterando de 0 a 5
    # fu
    for i in range(5):
        print(f"Valor do for: {i}")
    else:
        print(f"Loop terminou")

    # usando enumerate, que devolve o índice junto do valor na lista
    for elemento in enumerate(alfabeto):
        index, letra = elemento;
        print(index, letra)

    # Usando while
    contador = 0

    while contador < 3:
        if contador == 2:
        # quando usa um break, todo o loop para
        # o else só é executado quando a condição do while é falsa
        # então, se é utilizado um break, o else é ignorado
            print("Aqui paramo")
            break

        print(f'{contador} Dentro do loop')
        contador = contador + 1
    else:
        print('Conseguiu terminar!')

    # Usando continue
    # programa pra printar apenas números pares
    num = 0

    while num < 10:
        num += 1
        
        if (num % 2) == 0:
            continue

        print(num)

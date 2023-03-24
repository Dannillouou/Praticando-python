def rodandoSets():
    #Usando conjuntos em cobrinha
    print("Um set (conjunto) é uma lista que os elementos não mudam, não tem ordem e as duplicações são consideradas como um elemento so:")
    matriculas = {190343, 190443, 190572, 190847, 190567, 190981}
    for matricula in matriculas:
        print(matricula)

    #adicionando valor no conjunto
    matriculas.add(190123)
    print(matriculas)
    print(type(matriculas))
    print("\n")
    print("\n")
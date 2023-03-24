def rodandoTuplas():
    #As tuplas, um tipo diferente de lista

    print("\n")
    #lista: com [], tupla: com ()
    print("Uma tupla é uma lista imutável")
    materias = ('AEDV', 'ICD', 'IC', 'Cálculo', 'GA', 'IC')

    for materia in materias:
        print(materia)

    #cortando tupla:
    print(materias[1:4])  #printa do 1 (sem incluir) ao 4 (incluso)

    #contando número de elementos ate um elemento específico
    print(materias.count('IC'))  #printa o número de vezes que o elemento aparece
    print(materias.index('IC')) #printa a primeira ocorrência do elemento

    print(materias)
    #Printando o tipo
    print(type(materias))
    print("\n")
    print("\n")
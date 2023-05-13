def rodandoDicionario():
    #Dicionário, a lista mai doidera que tem
    print("Dicionário é uma lista de itens que são identificados por uma chave, que serve como seu índice:")

    estados = {'MG': 'Beaga', 'RJ': 'Rio de Janeiro', 'SP': 'São Paulo', 'ES': 'Vitória'}
    print(estados)
    print(estados['MG'])
    #adicionando valor
    estados['PR'] = 'Curitiba'
    print('printando chaves')
    for chave in estados.keys():
        print(chave)
    print('printando valores:')
    for valores in estados.values():
        print(valores)
    print('printando itens')
    for item in estados.items():
        print(item)

    # iterando por duas listas ao mesmo tempo
    print(type(estados))

    # dicionário aninhado
    dicionario_aninhado = {"Universidade" : "FGV", "Escolas" : {1 : "EMAp", 2 : "EBAPE", 3 : "DIREITO RIO"}}
    print(dicionario_aninhado.values())

    # criando dicionario por lista de tuplas
    dicionario_criado_por_funcao = dict(
        [
            (1, "EMAp"),
        (2, "EBAPE"), 
        (3, "DIREITO RIO")
        ]
    )

    try:
        print(dicionario_aninhado["Escolas"][4])
    except KeyError: # erro gerado quando a chave acessada não existe
        print("Chave não existe")

    # o "in" verifica a existência de chave, não de valor
    print(1 in dicionario)
    print("EMAp" in dicionario)

rodandoDicionario()
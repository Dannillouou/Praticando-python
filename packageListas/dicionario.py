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

rodandoDicionario()


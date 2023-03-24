def rodandoDicionario():
    #Dicionário, a lista mai doidera que tem
    print("Dicionário é uma lista de itens que são identificados por uma chave, que serve como seu índice:")

    estados = {'MG': 'Beaga', 'RJ': 'Rio de Janeiro', 'SP': 'São Paulo', 'ES': 'Vitória'}
    print(estados)
    print(estados['MG'])
    #adicionando valor
    estados['PR'] = 'Curitiba'
    chaves = estados.keys()
    estadosList = list(estados.items())
    print('printando chaves:')

    #iterando por duas listas ao mesmo tempo
    for cidade, estado in zip(estadosList, chaves):
        print(f'{estado}  {cidade}')
    print(type(estados))

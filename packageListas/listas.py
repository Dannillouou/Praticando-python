def rodandoListas():
    #Usando a grande de famigerada lista
    print("Listas são sequencias de dados. Em python tanto seus elementos quanto sua ordem são mutáveis")
    linguagens = ["swift", "java", "python", "c", "html", "css", "php", "dart"]
    #acessando
    for linguagem in linguagens:
        print(linguagem)

    #acesso negativo: conta a lista de tras pra frente
    print(linguagens[-2])

    #cortando lista
    print(linguagens[3:6])
    #começando do fim
    print(linguagens[:])

    #adicionando elementos
    linguagens.append("c++")
    print(linguagens)

    #adicionando toda a lista a outra
    frameworks = ["cake", "flutter", "bootsrap"]
    print(frameworks)
    frameworks.extend(linguagens)
    print(frameworks)

    #mudando valor de lista
    linguagens[-1] = "C#"
    print(linguagens)

    #removendo itens
    del linguagens[-1] #remove o último
    linguagens.remove('swift')
    print(linguagens)

    #vendo se elemento existe na lista
    print('C#' in linguagens)
    print('python' in linguagens)

    #tamanho da lista
    print('Tamanho da lista: ', len(linguagens))

    #printando tipo da lista
    print(type(linguagens))

def rodandoStrings():
    #brincando com strings
    #Concatenando strings
    greet = "Hello, "
    name = "Jack"

    #usando o operador +
    result = greet + name
    print(result)

    greet = 'Hello'
    #iterando através string greet
    #as strings funcionam como uma lista de caracteres
    for letter in greet:
        print(letter)

        greet = 'Hello'

    #Contando a quantidade de caracetres, o comprimento, da string
    print(len(greet))

    print('a' in 'program') #Como se tivesse um if implicito, printa true
    print('at' not in 'battle') #Printa false, pois olha se não tem "at" em "battle
    # multiline string 
    rickRoll = """Never gonna give you up
    Never gonna let you down"""

    primeiro_nome = (input("Digite seu primeiro nome: "))
    sobrenome = (input("Digite seu sobrenome: "))
    idade = (input("Digite sua idade: "))
    f_string = f"O seu nome é {primeiro_nome} {sobrenome} e voce tem {idade} anos!"

    print("essa é a grande f string:\n ", f_string)
    print(type(f_string))

    print(rickRoll)
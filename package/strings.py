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

    print(rickRoll)
<<<<<<< HEAD
#adicionando o caminho para modulo de variaveis
import sys

#caminho para o módulo de variaveis
sys.path.append('e:/Users/B51995/Desktop/Praticando-python/package')

#Módulo com variaveis
import variables

#Função para simplesmente falar a coisa mais importante da programação
def saudacao():
    print("Hello world!")

#criar função com valores padrões
def subtraiNumeros(a = 10,  b = 8):
    sum = a - b
    print('Sum:', sum)

#Recursividade
def fatorial(x):
    """Função recursiva para calcular o valor de um fatorial"""

    if x == 1:
        return x
    else:
        return (x * fatorial(x-1))

def rodandoFuncoes():
    # #Funções
    # #chamando com dois argumentos
    # subtraiNumeros(5, 3)#printa 2

    # #chamando com um argumento
    # #o outro vai pelo automático
    # subtraiNumeros(a = 20)#printa 12

    # #chamando argumento
    # subtraiNumeros()#printa 2

    # #A profundidade máxima é de 1000 recursividades, após isso o python corta para evitar recursividade infinita
    # num = 100
    # print("O fatorial de", num, "é: ", fatorial(num))

    # #função lambda
    # nome = input("Qual o seu nome? ")
    # #lambda que aceita um argumento
    # saudarUsuario = lambda Lamb_nome : print('Bom dia, ', Lamb_nome, '!')
    # #chamando lambda
    # saudarUsuario(nome)

    # #funções lambdas podem ser usadas como uma função de uma única
    # #expressão que pode mudar ligeiramente sua funcionalidade dentro de funções maiores

    # #Arquivo com todas as funções doiderinhas que eu criei p esse código

    # argumento que aceita inumeros valores e transfomra numa tupla
    # def soma_arbitraria(*numeros, inicio = 0) -> int:
    #     resultado = inicio
        
    #     for numero in numeros:
    #         resultado += numero
        
    #     return resultado
    
    # # the same
    # # print(sum([1,2,3,4,5,6,7,8,9,10], 10))
    # # print(soma_arbitraria(1,2,3,4,5,6,7,8,9,10))
    # numeros = (1,2,3,4,5,6,7,8,9,10)
    # print(sum(numeros, 100))
    # print(soma_arbitraria(1,2,3,4,5,6,7,8,9,10))
    # print(soma_arbitraria(1,2,3,4,5,6,7,8,9,10, inicio = 100))

    def soma_arbitraria_2(inicio = 0, *numeros) -> int:
        resultado = inicio

        for numero in numeros:
            resultado += numero
        
        return resultado
    
    print(soma_arbitraria_2(-10, 1,2,3,4,5,6,7,8,9,10))

    # funções que podem receber muitos argumentos
    def alunos_bons(escola, **alunos):
        print(escola)
        for cada_aluno in alunos:
            print(cada_aluno, end=" ")

=======
#adicionando o caminho para modulo de variaveis
import sys

#caminho para o módulo de variaveis
sys.path.append('e:/Users/B51995/Desktop/Praticando-python/package')

#Módulo com variaveis
import variables

#Função para simplesmente falar a coisa mais importante da programação
def saudacao():
    print("Hello world!")

#criar função com valores padrões
def subtraiNumeros(a = 10,  b = 8):
    sum = a - b
    print('Sum:', sum)

#Recursividade
def fatorial(x):
    """Função recursiva para calcular o valor de um fatorial"""

    if x == 1:
        return x
    else:
        return (x * fatorial(x-1))

def rodandoFuncoes():
    # #Funções
    # #chamando com dois argumentos
    # subtraiNumeros(5, 3)#printa 2

    # #chamando com um argumento
    # #o outro vai pelo automático
    # subtraiNumeros(a = 20)#printa 12

    # #chamando argumento
    # subtraiNumeros()#printa 2

    # #A profundidade máxima é de 1000 recursividades, após isso o python corta para evitar recursividade infinita
    # num = 100
    # print("O fatorial de", num, "é: ", fatorial(num))

    # #função lambda
    # nome = input("Qual o seu nome? ")
    # #lambda que aceita um argumento
    # saudarUsuario = lambda Lamb_nome : print('Bom dia, ', Lamb_nome, '!')
    # #chamando lambda
    # saudarUsuario(nome)

    # #funções lambdas podem ser usadas como uma função de uma única
    # #expressão que pode mudar ligeiramente sua funcionalidade dentro de funções maiores

    # #Arquivo com todas as funções doiderinhas que eu criei p esse código

    # argumento que aceita inumeros valores e transfomra numa tupla
    # def soma_arbitraria(*numeros, inicio = 0) -> int:
    #     resultado = inicio
        
    #     for numero in numeros:
    #         resultado += numero
        
    #     return resultado
    
    # # the same
    # # print(sum([1,2,3,4,5,6,7,8,9,10], 10))
    # # print(soma_arbitraria(1,2,3,4,5,6,7,8,9,10))
    # numeros = (1,2,3,4,5,6,7,8,9,10)
    # print(sum(numeros, 100))
    # print(soma_arbitraria(1,2,3,4,5,6,7,8,9,10))
    # print(soma_arbitraria(1,2,3,4,5,6,7,8,9,10, inicio = 100))

    def soma_arbitraria_2(inicio = 0, *numeros) -> int:
        resultado = inicio

        for numero in numeros:
            resultado += numero
        
        return resultado
    
    print(soma_arbitraria_2(-10, 1,2,3,4,5,6,7,8,9,10))

    # funções que podem receber muitos argumentos
    def alunos_bons(escola, **alunos):
        print(escola)
        for cada_aluno in alunos:
            print(cada_aluno, end=" ")

>>>>>>> 0d9e00442ffac865ba01f89ae3f5cdeca6d6887c
rodandoFuncoes()
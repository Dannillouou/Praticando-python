#Arquivo com todas as funções doiderinhas que eu criei p esse código

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
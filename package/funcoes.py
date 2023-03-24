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
    #Funções
    #chamando com dois argumentos
    subtraiNumeros(5, 3)#printa 2

    #chamando com um argumento
    #o outro vai pelo automático
    subtraiNumeros(a = 20)#printa 12

    #chamando argumento
    subtraiNumeros()#printa 2

    #A profundidade máxima é de 1000 recursividades, após isso o python corta para evitar recursividade infinita
    num = 100
    print("O fatorial de", num, "é: ", fatorial(num))

    #função lambda
    nome = input("Qual o seu nome? ")
    #lambda que aceita um argumento
    saudarUsuario = lambda Lamb_nome : print('Bom dia, ', Lamb_nome, '!')
    #chamando lambda
    saudarUsuario(nome)

    #funções lambdas podem ser usadas como uma função de uma única
    #expressão que pode mudar ligeiramente sua funcionalidade dentro de funções maiores

    #Arquivo com todas as funções doiderinhas que eu criei p esse código

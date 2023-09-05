# imports
# imports devem sempre estar no topo do codigo, seguindo a seuginte ordem:
# 1. imports de bibliotecas base do python
# 2. imports de terceiros relacionados
# 3. imports especificos locais criados no programa
# e entre cada grupo de imports deve haver uma linha vazia

# imports de diferentes bibliotecas devem ser em linhas diferentes
import numpy
import pandas
# mas dois modulos dentro de uma biblioteca na mesma linha
from subprocess import Popen, PIPE

# imports absolutos sao recomendados
import mypkg.sibling
from mypkg import sibling
from mypkg.sibling import example

# coringas ("*") devem ser evitados

#================================================================================
# Identacao: 4 espaços

# Separamos argumentos do corpo da funcao com o dobro da indentação
# para os argumentos. Muitos argumentos em um nome longo devem ser
# separados em multiplas linhas, começando depois do nome da função
def funcao_com_nome_longo(
        argumento1, argumento2, 
        argumento3, argumento4):
    argumento3 = argumento1 + argumento2
    return argumento3

#=============================================================
isso_eh_uma_coisa = True
isso_eh_outra_coisa = True

# indentação de if's
if (isso_eh_uma_coisa 
        and isso_eh_outra_coisa):
    print(isso_eh_uma_coisa)

#=============================================================
# indentacao de construtores
lista = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]

#=============================================================
"""
Cada linha deve ter no máximo 79 caracteres.
Com comentários e documentação a 72 
Configuração no visual studio code:
"editor.rulers": [
        80
    ]
"""

#=============================================================
# em expressões muito longas de abertura de arquivos, podemos usar uma
# barra para separar as diferentes expressões
with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())

#=============================================================
# para vários operadores matemáticos de uma vez
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)

#=============================================================
# classes e funções importantes cercados por duas linhas vazias


class ClasseImportante():
    _importante = True
    _atributo_1 = ""
    _atributo_2 = 0
    _atributo_3 = 3.14

    def __init__(self) -> None:
        pass


def funcao_importante(coisa_importante) -> ClasseImportante:
    classe_importante = ClasseImportante
    return classe_importante


# blocos de funcoes relacionadas devem ser separados por linhas vazias
def funcao_aleatoria() -> None:
    print("sou uma função")
    print("faco coisas de funcoes")
    
    #linhas vazias cercando blocos logicos
    if True:
        print("A verdade nunca é mentira")
funcao_aleatoria()

# varias implementacoes sem muito sentido em linhas unicas ficam juntas
print("print 1")
print("print 2")
print("print 3")
x = 3
y = 12.13

#=============================================================
# trailing commas:
# virgulas ao fim de toda linha de uma estrutura de dados, de forma que
# adicionar um valor ao fim da estrutura é igual a adicionar um valor no 
# meio da mesma
# exemplo:
capitals = {
    'China': 'Beijing',
    'India': 'New Delhi',
    'Mexico': 'Mexico City',
}
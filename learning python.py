#Comentários são feitos assim
#Arquivozinho de cria pra anotar varias coisas uteis de python p usar

#importando arquivo de variáveis
import variables
#importando arquivo com funções
import functions as func
#importando todos trens do package de matemática
from math import *
#parece ser problemático, pois acaba que meio que são criadas várias variáveis com so valores de dentro do import

#modulos e packages --> modulos são o arquivo py, enquanto o package é tem o arquivo __init__

#Criando a melhor função possível p começar bem:
func.saudacao()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Usando arquivo com variaveis salva por fora
print("Variáveis do arquivo de variáveis")
print(variables.PI)
print(variables.AC_GRAVIDADE)
print(variables.abelha)
print(f"Torta? {pi}") #usando o pi definido em math
print("\n")
print("\n")

#Tipos de variáveis
#Numéricos
print("Tipos de variáveis")
num1 = 5
print(num1, type(num1))

num2 = 2.0
print(num2, type(num2))

num3 = 1+2j
#a parte complexa é feita com "j"
print(num3, type(num3))

print("\n")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#As tuplas, um tipo diferente de lista

print("\n")
#lista: com [], tupla: com ()
print("Uma tupla é uma lista imutável")
materias = ('AEDV', 'ICD', 'IC', 'Cálculo', 'GA', 'IC')

for materia in materias:
    print(materia)

#cortando tupla:
print(materias[1:4])  #printa do 1 (sem incluir) ao 4 (incluso)

#contando número de elementos ate um elemento específico
print(materias.count('IC'))  #printa o número de vezes que o elemento aparece
print(materias.index('IC')) #printa a primeira ocorrência do elemento

print(materias)
#Printando o tipo
print(type(materias))
print("\n")
print("\n")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Usando conjuntos em cobrinha
print("Um set (conjunto) é uma lista que os elementos não mudam, não tem ordem e as duplicações são consideradas como um elemento so:")
matriculas = {190343, 190443, 190572, 190847, 190567, 190981}
for matricula in matriculas:
    print(matricula)

#adicionando valor no conjunto
matriculas.add(190123)
print(matriculas)
print(type(matriculas))
print("\n")
print("\n")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Input e output na cobrinha

#print "avançado"
#sep padrão= ' '
#end padrão= '\n'
print('printizinho de cria', 2023, 'muito foda', variables.hello, sep=',', end='\n\n')
print('printizinho de cria', 2023, 'muito foda e esse sem end', variables.hello, sep=', ')
print('printizinho de cria sem sep', 2023, 'muito foda', variables.hello,)

#input
receber = input('Digite algo: ')
print(receber)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Operadores doidera de comparação
x = 'Hello world'
y = {1:'a', 2:'b'}

# Olha se 'H' está presente. É case sensitive
print('H' in x)  # prints True

# check if 'hello' is present in x string
print('hello' not in x)  # prints True

# check if '1' key is present in y
print(1 in y)  # prints True

# check if 'a' key is present in y
print('a' in y)  # prints False

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Usando variável global 
#define global variable 
global_var = 10

def my_function():
    # define local variable
    local_var = 20

    # modify global variable value 
    global global_var
    global_var = 30

# print global variable value
print(global_var)

# call the function and modify the global variable
my_function()

# print the modified value of the global variable
print(global_var)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Estruturas de repetição
#usando else if
number = 0

if number > 0:
    print("Positive number")

elif number == 0:
    print('Zero')
else:
    print('Negative number')

#usando emoji
print('Pyhton usa elif mano que trem feio \U0001F922')

#Usando for
#Iterando de 0 a 5
#fu
for i in range(5):
    print(f"Valor do for: {i}")
else:
    print(f"Loop terminou")

#Usando while
contador = 0

while contador < 3:
    if contador == 2:
    #quando usa um break, todo o loop para
    #o else só é executado quando a condição do while é falsa
    #então, se é utilizado um break, o else é ignorado
        print("Aqui paramo")
        break

    print(f'{contador} Dentro do loop')
    contador = contador + 1
else:
    print('Conseguiu terminar!')

#Usando continue
#programa pra printar apenas números pares
num = 0

while num < 10:
    num += 1
    
    if (num % 2) == 0:
        continue

    print(num)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Usamos a palavra-chave pass para permitir que um bloco de código com algo 
#que ainda vai ser feito execute, mesmo sem fazer nada, sem gerar um erro, como de identação, por exemplo
n = 11

if n > 10:
    pass

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Funções
#chamando com dois argumentos
func.subtraiNumeros(5, 3)#printa 2

#chamando com um argumento
#o outro vai pelo automático
func.subtraiNumeros(a = 20)#printa 12

#chamando argumento
func.subtraiNumeros()#printa 2

#A profundidade máxima é de 1000 recursividades, após isso o python corta para evitar recursividade infinita
num = 100
print("O fatorial de", num, "é: ", func.fatorial(num))

#função lambda
nome = input("Qual o seu nome? ")
#lambda que aceita um argumento
saudarUsuario = lambda Lamb_nome : print('Bom dia, ', Lamb_nome, '!')
#chamando lambda
saudarUsuario(nome)

#funções lambdas podem ser usadas como uma função de uma única
#expressão que pode mudar ligeiramente sua funcionalidade dentro de funções maiores

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Variável não-local

#função de fora 
def fora():
    message = 'local'

    #função de dentro  
    def dentro():
        #variável não-local
        nonlocal message

        message = 'não-local'
        print("drento:", message)

    dentro()
    print("fora:", message)

fora()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#brincando com modules
#listar os bgl dentro de um modulo
funcoes = dir (func)

#listar as variaveis modulos e os caralha4
print(dir())
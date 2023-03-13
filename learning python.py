# comentários são feitos assim

#importando arquivos de variáveis
import variables

#multiplos valores para multiplas variaveis
print("Variáveis aleatórias")
a, b, c, d = 5, 3.2, 'Hello', None
print(a)  # prints 5
print(b)  # prints 3.2
print(c)  # prints Hello
print(d)  # prints none
print("\n")
print("\n")
#printando as variaveis do arquivo de variaveis
print("Variáveis do arquivo de variáveis")
print(variables.PI)
print(variables.AC_GRAVIDADE)
print(variables.abelha)
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

#Lista
#lista
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

print(type(linguagens))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print("\n")
#Tupla
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
print(type(materias))
print("\n")
print("\n")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#string
string = 'Isso é uma string'
print(string)

print("\n")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#set
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

#dictionary
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
#input e output
#print "avançado"
#sep padrão= ' '
#end padrão= '\n'
print('printizinho de cria', 2023, 'muito foda', c, sep=',', end='\n\n')
print('printizinho de cria', 2023, 'muito foda e esse sem end', c, sep=', ')
print('printizinho de cria sem sep', 2023, 'muito foda', c,)

#input
receber = input('Digite algo: ')
print(receber)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#operadores doidera de comparação
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

# define global variable 
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
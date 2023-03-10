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

#Lista
#lista
print("Listas são sequencias de dados. Em python tanto seus elementos quanto sua ordem são mutáveis")
linguagens = ["swift", "java", "python", "c", "html", "css", "php", "dart"]
#acessando
for linguagem in linguagens:
    print(linguagem)

print(linguagens)
print(type(linguagens))

print("\n")
#Tupla
#lista: com [], tupla: com ()
print("Uma tupla é uma lista imutável")
materias = ('AEDV', 'ICD', 'IC', 'Cálculo', 'GA')

for materia in materias:
    print(materia)

print(materias)
print(type(materias))
print("\n")
print("\n")

#string
string = 'Isso é uma string'
print(string)

print("\n")

#set
print("Um set (conjunto) é uma lista que os elementos não mudam, não tem ordem e as duplicações são consideradas como um elemento so:")
matriculas = {190343, 190443, 190572, 190847, 190567, 190981}
for matricula in matriculas:
    print(matricula)

print(matriculas)
print(type(matriculas))
print("\n")
print("\n")

#dictionary
print("Dicionário é uma lista de itens que são identificados por uma chave, que serve como seu índice:")

estados = {'MG': 'Beaga', 'RJ': 'Rio de Janeiro', 'SP': 'São Paulo', 'ES': 'Vitória'}
print(estados)
print(estados['MG'])
chaves = estados.keys()
print('printando chaves:')

for (estado, cidade) in zip(chaves, estados):
    print(estado, ' | ', cidade)
print(type(estados))


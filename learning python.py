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
print("Lista")
linguagens = ["swift", "java", "python", "c", "html", "css", "php", "dart"]
#acessando
for linguagem in linguagens:
    print(linguagem)

print(linguagens)
print(type(linguagens))

print("\n")
#Tupla
#lista: com [], tupla: com ()
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


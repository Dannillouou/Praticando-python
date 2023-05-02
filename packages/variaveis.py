# Esse arquivo tem nome diferente para indicar que aqui eu apenas brinquei
# com variáveis e usei o outro module para salver outras variáveis como se fosse
# o principal para salvar variáveis

# importando modulo de outra pasta com o modulo sys
import variables
import sys
sys.path.append('e:/Users/B51995/Desktop/Praticando-python/package')

# arquivo "oficial com varivaies salvas"

# Usando arquivo com variaveis salva por fora
print("Variáveis do arquivo de variáveis")
print(variables.PI)
print(variables.AC_GRAVIDADE)
print(variables.abelha)
pi = variables.PI
print(f"Torta? {pi}")  # usando o pi definido em math
print("\n")
print("\n")

# Tipos de variáveis
# Numéricos
print("Tipos de variáveis")
num1 = 5
print(num1, type(num1))

num2 = 2.0
print(num2, type(num2))

num3 = 1+2j
# a parte complexa é feita com "j"
print(num3, type(num3))

print("\n")


#=====================strings==================================

# brincando com strings
# Concatenando strings
greet = "Hello, "
name = "Jack"

# usando o operador +
result = greet + name
print(result)

greet = 'Hello'
# iterando através string greet
# as strings funcionam como uma lista de caracteres
for letter in greet:
    print(letter)

    greet = 'Hello'

# Contando a quantidade de caracetres, o comprimento, da string
print(len(greet))

print('a' in 'program')  # Como se tivesse um if implicito, printa true
# Printa false, pois olha se não tem "at" em "battle
print('at' not in 'battle')
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
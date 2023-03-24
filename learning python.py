#Comentários são feitos assim
#Arquivozinhos de cria pra anotar varias coisas uteis de python p usar

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Fazendo imports de diferentes pastas
#tem duas formas de fazê-lo

#alterando o module interno sys, onde alteramos o sys.path, que, equivalentemente ao path do windows
#é onde o programa olha para procurar por coisas importantes como os modules
import sys
#como o sys.path é uma lista, podemos simplesmente adicionar o caminho do novo módulo
sys.path.append('e:/Users/B51995/Desktop/Praticando-python/packageListas')
sys.path.append('e:/Users/B51995/Desktop/Praticando-python/package')

#agora, chamamos os módulos como se nada tivesse acontecido
import variables

#É possível também, pelo terminal, mudar a variável de ambiente PYTHONPATH, mas eu preferi usar só
#a forma que pode ser feita dentro do código

#Mesmo que de um warning, isso ocorre porque o pre-analisador não entende que os modulos podem estar em outra pasta, mas por enquanto eu acho que nao tem problema
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Import para manipulação dos arquivos do sistema
import os

#importando arquivo com funções
#coloquei o antigo módulo functions dentro de funções
import funcoes as func

#modulos e packages --> modulos são o arquivo py, enquanto o package tem o arquivo __init__

#imports de todos os modulos/arquivos com todo o código ja escrito para organizar
#cada módulo faz uma coisa diferente e tem uma função que roda todo o código


#Começando bem:
func.saudacao()

#Usamos a palavra-chave pass para permitir que um bloco de código com algo 
#que ainda vai ser feito execute, mesmo sem fazer nada, sem gerar um erro, como de identação, por exemplo
n = 11

if n > 10:
    pass

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#brincando com modules
#listar os bgl dentro de um modulo
funcoes = dir (func)

#listar as variaveis modulos e os caralha4
print(dir())

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Usando outras bases decimais
print(0b1101011)  # printa 107 em binário

print(0xFB + 0b10)  # soma hexadecimal com binpario = printa 253

print(0o15)  # printa 13 em octal

#binário: 0b ou 0B
#octal: 0o ou 00
#hexadecimal: 0x ou 0X

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# multiline string 
rickRoll = """Never gonna give you up
Never gonna let you down"""

print(rickRoll)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#brincando com arquivos

"""try: #tenta executar
  #Tratamento de exceção é uma boa prática, pois nem sempre a
  #abertura de arquivos pode funcionar
  
  #abrindo arquivo - retorna um objeto de arquivo
  #padrão read - r
  #modos: r - leitura, w - escrita, a - append
  arquivo = open("coltec.txt", "r")

  conteudo = arquivo.read(6)
  print(conteudo)

  maisConteudo = arquivo.read(5)
  print(maisConteudo)
finally: #sempre é executado no fim
  arquivo.close

with open("coltecEscreve.txt", "w") as coltec:
  #A função with faz o tratamento de exceção especificamente 
  #para arquivos abertos, fazendo o try e colocando o 
  #fechamento no finally
  
  coltec.write("Coltec!\n")
  coltec.write("ELITEEEE")

with open("coltecEscreve.txt", "r+") as coltec:
  #A função with faz o tratamento de exceção especificamente 
  #para arquivos abertos, fazendo o try e colocando o 
  #fechamento no finally
  
  mensagem = input("O que você tem a dizer sobre o coltec? ")
  coltec.write("\n\nMensagem para o coltec do usuário:")
  coltec.write("\n" + mensagem)

  #voltando para o começo do arquivo para poder lê-lo:
  arquivo.seek(0)
  
  linhas = coltec.readlines()
  #recupera lista com todas as linhas
  print(linhas)

  #de novo...
  arquivo.seek(0)
  
  #Printando lista de linhas no arquivo
  linhas.append("Desculpa repeti a mensagem tava muito emocionado e com sono, nem vi")
  coltec.writelines(linhas)

#funcionou quase como o esperado, mas deu p entender a ideia

#Manipulando diretórios
# change directory
os.chdir('E:\\Users\B51995')
diretorioAtual = os.getcwd()
print(diretorioAtual)

listaDiscoC = os.listdir('C:\\')
print(listaDiscoC)

os.chdir(diretorioAtual + '\Desktop')
#criando diretorio
os.mkdir('teste')
os.rename('teste', 'novoDir')
os.chdir('novoDir')

with open("testezin.txt", "w") as arquivo:
    arquivo.write('Arquivo novo p deletar fodas')
    #deletando arquivo
os.chdir("testezin.txt")
os.rmdir(os.getcwd())"""

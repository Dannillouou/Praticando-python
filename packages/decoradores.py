# em python um decorador é um padrão de design
# que permite modificar as funcionalidades de uma função
# encapsulando ela em outra função

# a função externa é um decorador, que usa a função original
# como parâmetro e e retorna uma verão modificada dela


# usando função como argumento de outra função
def adicao(a, b):
    return a + b

def calcular(funcao, a, b):
    return funcao(a, b)

a = 5
b = 10

print(calcular(adicao, a, b)) # printa a + b

# retornando função em outra função
def saudacoes(nome_usuario):
    def ola():
        return "Olá " + nome_usuario + "!"
    # retornando funcao
    return ola()

saudar = saudacoes("frangolino")
print(saudar)

# basicamente, qualquer objeto que tenha o método __call__()
# é um "chamável" (callable). Então um decorador é um "chamável"
# que chama outro "chamável

def deixa_bonito(funcao):
    def interna():
        print("Eu fui embelezada!")

        funcao()

    return interna

def comum():
    print("Eu sou uma funcao comum")

def diferenciada():
    print("Eu sou uma funcao diferenciada")

# função decoradas
comum_embelezada = deixa_bonito(comum)
diferenciada_embelezada = deixa_bonito(diferenciada)

comum_embelezada()# printa o embelezamento e a função logo depois
diferenciada_embelezada()# printa o embelezamento e a função logo depois

# ao invés de sempre colocar a função numa variável sempre,
# o python tem uma forma bem mais elegante de fazer essa funcionalidade:

# funciona da mesma forma, e só chamamos a função que foi alterada
print("\n\n usando decorador de forma mais bonita")
@deixa_bonito
def normalzinha():
    print("eu sou normalzinha")

normalzinha()

# usando decoradores com funções que recebem parâmetros
print("\n\nUsando mais de um decorador")

def divisao_inteligente(funcao_divisao):
    def interna(a, b):
        print("Vou dividir", a, "e", b)

        if b == 0:
            print("Opa, nao vai ta rolando meu mano")
            return
        else:
            return funcao_divisao(a, b)
    
    return interna

@divisao_inteligente
def divisao(a, b):
    return a / b

print(divisao(10,2))# retorna a divisão
print(divisao(4,0))# retorna nada

# usando dois decoradoes sucessivamente
def estrela(funcao):
    def interna(*args, **kwargs):
        print("*" * 15)
        funcao(*args, **kwargs)
        print("*" * 15)
    return interna

def porcento(funcao):
    def interna(*args, **kwargs):
        print("%" * 15)
        funcao(*args, **kwargs)
        print("%" * 15)
    return interna

@estrela
@porcento
def printa_mensagem(mensagem):
    print(mensagem)
# equivalente a printa_mensagem = estrela(porcento(printa_mensagem))

printa_mensagem("ei blz")
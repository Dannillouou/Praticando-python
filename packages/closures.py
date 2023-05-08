# # a ideia de closures é permitir o acesso de variáveis de uma função
# # mesmo depois dela ter sido executada. Pois sempre que uma função é executada
# # as variáveis são locais, só existem dentro dela e são deletadas logo depois

# def saudar():
#     nome = "João"

#     return lambda: "Olá, " + nome + "!"

# mensagem = saudar()

# print(mensagem())
# print(mensagem())
# print(mensagem())

# a função interna permite que, mesmo depois que a função eterna
# tenha sido chamada, os valores ainda possam ser acessados, pois
# a função que é executada é a interna
def calcular():
    numero = 1
    def funcao_interna():
        nonlocal numero
        numero += 2
        return numero
    return funcao_interna

# chamando função externa
impar = calcular()

# chamando função externa
print(impar()) # printa 3
print(impar()) # printa 5
print(impar()) # printa 7

# chamando função externa novamente
impar2 = calcular()
print(impar2()) # printa 3
dicionario = {"a":1, "b":2, "c":3, "d":8, "e": 16, "f":8, "g":3} 

# lista_valores = list(dicionario.values())

# maior = lista_valores[0]
# menor = lista_valores[0]

# for valor in lista_valores:
#     if valor > maior:
#         maior = valor
#     elif valor < menor:
#         menor = valor
        
# print(maior)
# print(menor)

# n = int(input("Insira o valor de n: "))

# dicionario = dict()

# for i in range(n):
#     dicionario[i + 1] = (i+1)**2
    
# print(dicionario)

# escrever função que remove valores duplicados de dicionario
# 

# def remove_duplicatas(dicionario):
#     chaves = list(dicionario.keys())
#     valores = list(set(dicionario.values()))
#     novo_dicionario = {}
#     for index in range(len(valores)):
#         novo_dicionario[chaves[index]] = valores[index]
        
#     return novo_dicionario

# #remove a primeira ocorrência dos valores        
# print(remove_duplicatas(dicionario))


def adicionar_pedido(numero_do_pedido, fila_de_pedidos):
    fila_de_pedidos.append(numero_do_pedido)
    print(f"Pedido {numero_do_pedido} adicionado")
    
def preparar_pedido(fila_de_pedidos):
    print(f"Pedido {fila_de_pedidos[0]} está pronto")
    fila_de_pedidos.remove(fila_de_pedidos[0])
          
def listar_pedidos_em_preparo(fila_de_pedidos):
    for pedido in fila_de_pedidos:
        print(f"Preparando {pedido}")
        
def verificar_pedido(numero_do_pedido, fila_de_pedidos):
    if fila_de_pedidos.count(numero_do_pedido) < 1:
        print(f"Pedido {numero_do_pedido} não existe")
        return
    else:
        print("Seu pedido é o número ", fila_de_pedidos.index(numero_do_pedido)+1, " na fila")
        
pedidos_em_preparo = []

# Driver code
adicionar_pedido(1, pedidos_em_preparo)
adicionar_pedido(2, pedidos_em_preparo)
adicionar_pedido(3, pedidos_em_preparo)
    
listar_pedidos_em_preparo(pedidos_em_preparo)

verificar_pedido(2, pedidos_em_preparo)
verificar_pedido(3, pedidos_em_preparo)

preparar_pedido(pedidos_em_preparo)# 1
preparar_pedido(pedidos_em_preparo)# 2

verificar_pedido(2, pedidos_em_preparo)
verificar_pedido(3, pedidos_em_preparo)

listar_pedidos_em_preparo(pedidos_em_preparo)
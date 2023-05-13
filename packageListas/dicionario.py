# def rodandoDicionario():
#     #Dicionário, a lista mai doidera que tem
#     print("Dicionário é uma lista de itens que são identificados por uma chave, que serve como seu índice:")

#     estados = {'MG': 'Beaga', 'RJ': 'Rio de Janeiro', 'SP': 'São Paulo', 'ES': 'Vitória'}
#     print(estados)
#     print(estados['MG'])
#     #adicionando valor
#     estados['PR'] = 'Curitiba'
#     print('printando chaves')
#     for chave in estados.keys():
#         print(chave)
#     print('printando valores:')
#     for valores in estados.values():
#         print(valores)
#     print('printando itens')
#     for item in estados.items():
#         print(item)
    # for item in estados.items():
    #     chave, valor = item
    #     print(f"{chave} -> {valor}")

#     # adicionando item no dicionário
#     novo_estado = dict()
#     novo_estado["SC"] = "Floripa"
#     estados.update(novo_estado)
#     print(estados)

#     # removendo um item do dicionario
#     # pela chave
#     del estados['ES']
#     print(estados)
#     # ultimo item
#     retirado = estados.pop('RJ')
#     print(estados)
#     print(retirado)
    
#     # se for dada uma chave que não existe e o segundo
#     # argumento for None, a função não levanta
#     retirado = estados.pop('AM', None)
#     print(estados)
#     print(retirado)

#     # deletando dicionario
#     try: 
#         del estados
#         print(estados)
#     except NameError:
#         print("Dicionario removido")

# rodandoDicionario()

#==============================================================================================

cartao = {}
cartao["Titular"] = "Marcelo Po"
cartao["Número"] = "1234 5678 1234 5678"

print(cartao)

cartao["Data de Vencimento"] = "31/02/2023"

print(cartao)

novos_dados = dict()

novos_dados["CVV"] = 120

cartao.update(novos_dados)
print(novos_dados)
print(cartao)

# vários tipos de dados
cartao["senha"] = 123456789
cartao["Ativo"] = True
cartao["Transacoes"] = [150, 20.0000000, 10, -580]

print(cartao)

for item in cartao:
    print(f"{item} -> {cartao[item]}")

for item in cartao.items():
    chave, valor = item
    print(f"{chave} -> {valor}")

# acessando transações
for valor in cartao["Transacoes"]:
    print(valor)

# acessando de forma segura por chave
print(cartao.get("CVV"))# retorna o valor salvo na chave "CVV"
print(cartao.get("Novachave"))# retorna None

novo_dicionario = dict()
novo_dicionario = "Da chave vazia"
# novo_dicionario["algo"] = "alguma coisa" não aceita
print(cartao)

new_set = {"A", "E", "I", "O", "U"}

# new_dict = dict(new_set) -> nao funfa
new_keys = (1,2, 3,4,5)

new_dict = dict(zip(new_set, new_keys))
print(new_dict)

# dicionário aninhado
dicionario_aninhado = {"Universidade" : "FGV", "Escolas" : {1 : "EMAp", 2 : "EBAPE", 3 : "DIREITO RIO"}}
print(dicionario_aninhado.values())

# criando dicionario por lista de tuplas
dicionario_criado_por_funcao = dict(
    [
        (1, "EMAp"),
        (2, "EBAPE"), 
        (3, "DIREITO RIO")
    ])

print(dicionario_criado_por_funcao)

try:
    print(dicionario_aninhado["Escolas"][4])
except KeyError: # erro gerado quando a chave acessada não existe
    print("Chave não existe")

# o "in" verifica a existência de chave, não de valor
print(1 in dicionario)
sprint("EMAp" in dicionario)

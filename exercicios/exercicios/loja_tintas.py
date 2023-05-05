# Tinta
# cobertura é de 1l/6m^2
# vendida em:
# latas de 18 l -> R$ 80,00
# galõs de 3,6 l -> R$ 25,00

# programa deve pedir metros^2 a serem pintados
# e responder a quantidade tinta a serem compradas em
# 1. apenas latas
# 2. apenas galões
# 3. latas e galões, com o menor desperdício de tinta
# acrescentando 10% de folga e arredondando para cima

# entendi que os 10% de folga devem ser apenas para o caso 3
#============================================================================================
# exceção personalizada que permite o recebimento apenas de modos de compra válidos
class ModoCompraDeTintaInvalido(Exception):
    # lançado quando o modo de compra de tinta
    # não é um dos três válidos

    # armazenando valor para possível uso futuro
    def __init__(self, valor) -> None:
        self.valor = valor

    def __str__(self) -> str:
        return (repr(self.value))

#============================================================================================
# # estrutura de repetição para permitir apenas o recebimento
# # de números
# valor_invalido = 1
# while valor_invalido:
#     try:
#         # recebendo tamanho da area a ser pintada
#         area_pintar = float(input("Digite a area (m^2) que será pintada: "))
#         # setando valor invalido como falso para sair do while
#         valor_invalido = 0
#     except ValueError:
#         print("Valor invalido, insira apenas numeros por favor")
#         continue

# # quantidade de tinta que vai ser necessária
# litros_de_tinta = area_pintar/3

# recebendo modo de compra com estrutura que impede o usuário
# de inserir valores inválidos
valor_invalido = 1
while valor_invalido:
    try:
        # recebendo o modo de compra
        # modo de compra de tinta, caso 1, 2 ou 3
        print("\nDigite a forma como quer comprar a tinta:") 
        print("\"latas\": para apenas latas;") 
        print("\"galoes\": para apenas galões; e")
        print("\"latas e galoes\": para misturar latas e galões ao mesmo tempo, com o menor desperdício.")
        modo_de_compra = str(input())
        if modo_de_compra != "latas" and modo_de_compra != "galoes" and modo_de_compra != "latas e galoes":
            raise ModoCompraDeTintaInvalido(modo_de_compra)
        valor_invalido = 0
    except ModoCompraDeTintaInvalido:
        print("\nInsira apenas uma das formas válidas de compra de tinta por favor")
        print("(\"latas\", \"galoes\", \"latas e galoes\")")
        continue

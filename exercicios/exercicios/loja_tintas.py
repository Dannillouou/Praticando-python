# arredondar números para cima
from math import ceil
# e para baixo
from math import floor

# Tinta
# cobertura é de 1l/6m^2
# vendida em:
# latas de 18 l -> R$ 80,00 -> 108 m^2 -> R$ 0,74/m^2
# galõs de 3,6 l -> R$ 25,00 -> 21,6 m^2 -> R$ 1,15/m^2

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

#variáveis
area_por_litros_de_tinta = 6
litros_lata = 18
litros_galao = 3.6
porcentagem_folga = 10
preco_lata = 80
preco_galao = 25

def calculaOrcamento(litros_de_tinta, modo_de_compra) -> tuple:
    numero_latas = 0
    numero_galoes = 0
    # fazendo os calculos
    # o arredondamento é feito para cima com math.ceil
    if modo_de_compra == "latas":
        numero_latas = ceil(litros_de_tinta/litros_lata)
        preco = numero_latas*preco_lata
        tupla = tuple([numero_latas, numero_galoes, preco])
        return tupla
        # print(f"numero de latas necessárias: {numero_latas}")
        # print(f"Orçamento: {preco}")

    elif modo_de_compra == "galoes":
        numero_galoes = ceil(litros_de_tinta/litros_galao)
        preco = numero_galoes*preco_galao
        
        tupla = tuple([numero_latas, numero_galoes, preco])
        return tupla
        # print(f"numero de galoes necessários: {numero_galoes}")
        # print(f"Orçamento: {preco}")

    elif modo_de_compra == "latas e galoes":
        # adicionando 10% de folga
        litros_de_tinta += litros_de_tinta/porcentagem_folga

        # arredondando para baixo o número de latas
        # pois a maior parte da tinta tem que vir de latas
        # e o os últimos > 18l de galoes
        numero_latas = floor(litros_de_tinta/litros_lata)

        # arredondando para cima número de galões para
        # não faltar tintta
        numero_galoes = ceil((litros_de_tinta % litros_lata)/litros_galao)

        preco = numero_latas * preco_lata
        preco += numero_galoes* preco_galao

        tupla = tuple([numero_latas, numero_galoes, preco])
        return tupla
        # print(f"numero de latas: {numero_latas}")
        # print(f"numero de galoes: {numero_galoes}")
        # print(f"Orçamento: {preco}")

def recebe_quantidade() -> int:
    # estrutura de repetição para permitir apenas o recebimento
    # de números
    valor_invalido = 1
    while valor_invalido:
        try:
            # recebendo tamanho da area a ser pintada
            area_pintar = float(input("Digite a area (m^2) que será pintada: "))
            # setando valor invalido como falso para sair do while
            valor_invalido = 0
        except ValueError:
            print("Valor invalido, insira apenas numeros por favor")
            continue

    # quantidade de tinta que vai ser necessária
    return area_pintar/area_por_litros_de_tinta

def recebe_modo() -> str:
    # recebendo modo de compra com estrutura que impede o usuário
    # de inserir valores inválidos
    valor_invalido = 1
    while valor_invalido:
        try:
            # recebendo o modo de compra
            # modo de compra de tinta, caso 1, 2 ou 3
            # menu
            print("\nDigite a forma como quer comprar a tinta:") 
            print("\"latas\": para apenas latas;") 
            print("\"galoes\": para apenas galões; e")
            print("\"latas e galoes\": para misturar latas e galões ao mesmo tempo, com o menor desperdício.")
            # recebimento
            modo_de_compra = str(input())

            # avaliação do recebimento do modo de compras
            if modo_de_compra != "latas" and modo_de_compra != "galoes" and modo_de_compra != "latas e galoes":
                raise ModoCompraDeTintaInvalido(modo_de_compra)
            # se não for lançada exceção sai do while
            valor_invalido = 0
        except ModoCompraDeTintaInvalido:
            # se for levantada exceção informa o erro ao usuário e tenta novamente
            print("\nInsira apenas uma das formas válidas de compra de tinta por favor")
            print("(\"latas\", \"galoes\", \"latas e galoes\")")
            continue
    return modo_de_compra

quantidade_latas, quantidade_galoes, preco = calculaOrcamento(recebe_quantidade(), recebe_modo())
print("Você vai precisar de:")
print(f"{quantidade_latas} latas")
print(f"{quantidade_galoes} galões")
print(f"Isso vai custar: R$ {preco}")
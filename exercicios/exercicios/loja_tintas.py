# importando funções do funcionamento do sistema
from funcoes_loja_tintas import *
#============================================================================================

quantidade_latas, quantidade_galoes, preco = calculaOrcamento(recebe_quantidade(), recebe_modo())
print("Você vai precisar de:")
print(f"{quantidade_latas} latas")
print(f"{quantidade_galoes} galões")
print(f"Isso vai custar: R$ {preco}")
# preços:
# Morango:
#   até 5 kg: 2,50/kg
#   mais de 5 kg: 2,20/kg
# Maçã:
#   até 5 kg: 1,80/kg
#   mais de 5 kg: 1,50/kg
# se um cliente comprar mais de 8kg de fruta ou mais de 25 reais,
# ainda é adicionado um desconto de 10% no preço final

#=============================================================================================

# funções gerais do sistema
def preco_morango(quantidade_kg) -> float:
    if quantidade_kg <= 5:
        return quantidade_kg * 2.5
    else: 
        return quantidade_kg * 2.2
    
def preco_maca(quantidade_kg) -> float:
    if quantidade_kg <= 5:
        return quantidade_kg * 1.8
    else: 
        return quantidade_kg * 1.5
    
def tem_desconto(quantidade_kg, preco):
    if quantidade_kg > 8 or preco > 25:
        return True

def recebendo_quantidade(fruta) -> int:
    valor_invalido = True
    while valor_invalido:
        try:
            quantidade_fruta = int(input(f"Quanto voce vai querer de {fruta} (kg)?"))
            valor_invalido = False
        except ValueError:
            print("Input invalido, tente novamente")
            continue

    return quantidade_fruta

print("Preços das frutas:")
print("Morango:")
print("até 5 kg: R$ 2,50/kg")
print("mais de 5 kg: R$ 2,20/kg")
print("Maçã:")
print("até 5 kg: R$ 1,80/kg")
print("mais de 5 kg: R$ 1,50/kg")
print("Você comprando mais de 8kg ou 25 reais, ainda tem um desconto de 10%")

# recebendo quantidade de morangos
quantidade_morangos = recebendo_quantidade("Morango")
# recebendo quantidade de maçãs
quantidade_macas = recebendo_quantidade("Maca")

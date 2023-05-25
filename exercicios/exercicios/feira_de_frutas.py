<<<<<<< HEAD
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
=======
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
    else:
        return False
    
def preco_total(preco_morangos, preco_macas):
    return preco_morangos + preco_macas

def preco_final(preco_total, tem_desconto) -> float:
    if tem_desconto:
        return preco_total - preco_total/10
    else:
        preco_total

def recebendo_quantidade(fruta) -> int:
    valor_invalido = True
    while valor_invalido:
        try:
            quantidade_fruta = int(input(f"\nQuanto voce vai querer de {fruta} (kg)? "))
            valor_invalido = False
        except ValueError:
            print("Input invalido, tente novamente")
            continue

    return quantidade_fruta

def menu_inicial():
    print("Preços das frutas:")
    print("Morango:")
    print("até 5 kg: R$ 2,50/kg")
    print("mais de 5 kg: R$ 2,20/kg")
    print("Maçã:")
    print("até 5 kg: R$ 1,80/kg")
    print("mais de 5 kg: R$ 1,50/kg")
    print("Você comprando mais de 8kg ou 25 reais, ainda tem um desconto de 10%")

#============================================================================================
#programa sendo rodado

#printando menu inicial
menu_inicial()
# recebendo quantidade de morangos
quantidade_morangos = recebendo_quantidade("Morango")
# recebendo quantidade de maçãs
quantidade_macas = recebendo_quantidade("Maca")
# quantidade total
quantidade_total = quantidade_morangos + quantidade_macas

preco_total = preco_total(preco_morango(quantidade_morangos), preco_maca(quantidade_macas))
tem_desconto = tem_desconto(quantidade_total, preco_total)
preco_final = preco_final(preco_total, tem_desconto)

if tem_desconto:
    print("\nVoce recebeu um desconto!:")
    print(f"O valor caiu de: R$ {preco_total}")
    print(f"Para: R$ {preco_final}")
else:
    print("O valor da sua compra é de: ", preco_final)
>>>>>>> 0d9e00442ffac865ba01f89ae3f5cdeca6d6887c

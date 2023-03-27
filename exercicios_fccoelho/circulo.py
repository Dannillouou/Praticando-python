import math as m

def area_circulo(radio):
    return m.pi * (radio ** 2)

radio = float(input("gimme da radio: "))

print(area_circulo(radio))
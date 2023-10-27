from enum import Enum

# cria uma constante, de certa forma
class Escolas(Enum):
    EMAp = 1
    EBAPE = 2
    DIREITO_RIO = 3

class Meses(Enum):
    JANEIRO = 1
    FEVEREIRO = 2
    MARCO = 3


print(Meses.JANEIRO)
print(Meses.JANEIRO.name)
print(Meses.JANEIRO.value)

# levanta erro: "cannot reassign member"
# Meses.JANEIRO = 5

print(type(Meses.JANEIRO)) # enum 'Meses'
print(type(Meses.JANEIRO.name))
print(type(Meses.JANEIRO.value))

print(Escolas.EMAp == Escolas.EBAPE)
print(Meses.FEVEREIRO.value > Meses.JANEIRO.value)
import documentation_module as dm

numero = 42

# verificando se numero é instância de inteiro e printa mensagem e levanta um 
# AssertionError caso o número não seja float assert isinstance(numero, float), 
# "Erro, tipo diferente recebido"

# para evitar erros, usamos diversas assertivas ao
# longo do código

def soma(a, b):
    assert isinstance(a, float), "Erro, tipo diferente recebido"
    # algoritmo
    assert isinstance(b, float), "Erro, tipo diferente recebido"
    pass

soma(12.0, 24.0)
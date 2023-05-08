# def rodandoSets():
#     # Usando conjuntos em cobrinha
#     # Um set (conjunto) é uma lista que os elementos não mudam, não tem ordem e as duplicações são consideradas como um elemento so:
#     matriculas = {190343, 190443, 190572, 190847, 190567, 190981}
#     for matricula in matriculas:
#         print(matricula)

#     #adicionando valor no conjunto
#     matriculas.add(190123)
#     print(matriculas)
#     print(type(matriculas))
#     print("\n")

set_vazio = set()
set_numeros = set(range(0,100))
print(set_numeros)

# remover duplicatas de uma lista
lista_pares = [2, 0, 4, 6, 8, 2, 10, 4]
lista_sem_duplicatas = list(set(lista_pares))
print(lista_sem_duplicatas)
import documentation_module as dm
"""
Principío da proximidade
O comentário deve estar o mais próximo possível do código ao qual se refere

Princípio da simplicidade

Principio da não-redundância
Ao documentar/comentar um código, devemos partir do pressuposto de que quem
está lendo o código conhece a linguagem, para evitarmos comentários redundantes

Princípio do código limpo

PEP8
"""

print(dm.juros_simples(10000, 15.18, 12))
print(dm.juros_compostos(10000, 15.18, 12))

help(dm)
class Aventureiro:
    def __init__(self, nome) -> None:
        self._nome = nome

class GrupoAventureiro:
    def __init__(self, nome) -> None:
        self._nome = nome
        self._aventureiros = []

guerreiro = Aventureiro("Átila, o Huno")  # Flagellum Dei
print(guerreiro)

# del guerreiro
# print(guerreiro)

feiticeiro = Aventureiro("Gandalf, o Branco") # Gandalf, o Alemão
print(feiticeiro)

grupo_aventureiros = GrupoAventureiro("Grupo dos Sonhos")
grupo_aventureiros._aventureiros.append(guerreiro)
grupo_aventureiros._aventureiros.append(feiticeiro)
print(grupo_aventureiros)
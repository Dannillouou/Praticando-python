# Has-a
# Tem-um


class Guerreiro:
    def __init__(self, nome) -> None:
        self._nome = nome
        self._arma = None

    def atacar(self):
        if self._arma is not None:
            print(f"{self._nome} ataca com {self._arma._nome} e causa ({self._arma._pontos_de_dano}) de dano")
        else:
            print(f"{self._nome} ataca com as e casa (1) ponto de dano")

    def equipar_arma(self, nome, dano):
        self._arma = Arma1M(nome, dano)

    def __del__(self):
        print(f"Removendo {self._nome}")

class Arma1M:
    def __init__(self, nome, dano) -> None:
        self._nome = nome
        self._pontos_de_dano = dano

    def __str__(self):
        return f"A arma \"{self._nome}\" causa ({self._pontos_de_dano}) pontos de dano"
    
    def __del__(self):
        print(f"Removendo {self._nome}")
    

guerreiro = Guerreiro("Miyamoto Musashi")
guerreiro.atacar()
guerreiro.equipar_arma("Wakizashi", 15)
guerreiro.atacar()

guerreiro.equipar_arma("Katana" ,25)
guerreiro.atacar()

# quando deletemos o guerreiro, a arma, que só existe junto dele, acaba ficando
# "perdida" no meio do código e, por isso, o garbage collector acaba com ela
del guerreiro
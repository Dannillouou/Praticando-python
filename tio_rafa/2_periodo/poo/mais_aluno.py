# modulo de classes abstratas
from abc import ABC, abstractmethod

# criando classe abstrata
class Aluno(ABC):
    def __init__(self) -> None:
        self.cr = 0

    # implementando método abstrato, que deve ser usado por uma classe derivada
    @abstractmethod
    def _estudar(self, disciplina): ...
    
    def realizar_prova(self, disciplina):
        print(f"Realizando prova de {disciplina}")

    @property
    @abstractmethod
    def cr(self): ...

class AlunoEMAp(Aluno):
    def _estudar(self, disciplina):
        print(f"Estudando - com afinco - {disciplina}")

aluno_emap = AlunoEMAp()
aluno_emap.realizar_prova("Linguagens de Programação")

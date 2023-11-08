class Aluno:
    def __init__(self, qi, nr_artigos_publicados) -> None:
        self.qi = qi
        self.nr_artigos_publicados = nr_artigos_publicados

    def __str__(self) -> str:
        return f"QI: {self.qi} e Publicações: {self.nr_artigos_publicados}"
    
    def __add__(self, other):
        qi_total = self.qi + other.qi
        publicações_acumuladas = self.nr_artigos_publicados + other.nr_artigos_publicados

        return Aluno(qi_total, publicações_acumuladas)
    
    def __gt__(self, other):
        if self.qi > other.qi:
            return True
        elif self.qi == other.qi:
            return self.nr_artigos_publicados > other.nr_artigos_publicados
        else:
            return False

aluno_medio = Aluno(100, 0)
aluno_pica = Aluno(130, 2)
super_aluno = aluno_medio + aluno_pica

print(aluno_medio)
print(aluno_pica)
print(super_aluno)

"""
if aluno_medio > aluno_pica:
    print("O aluno 1 é MELHOR que o aluno 2")
else:
    print("O aluno 2 é MELHOR que o aluno 1")
"""
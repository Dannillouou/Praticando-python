class EMAp:
    def __new__(cls, *args, **kwargs):
        print("Podemos fazer o que quisermos antes da instância")
        object_ = super().__new__(cls)
        print("Podemos fazer o que quisermos depois da instância")
        return object_


    def __init__(self, nr_alunos) -> None:
        self.nr_alunos = nr_alunos

escola = EMAp(42)
print(escola.nr_alunos)


# esse código é rodado antes do init
# é criado um objeto com __new__, que depois é passado para o __init__
escola_como_um_homem = object().__new__(EMAp)
print(escola_como_um_homem)
escola_como_um_homem.__init__(666)
print(escola_como_um_homem)
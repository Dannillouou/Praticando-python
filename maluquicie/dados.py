import os
import sys

def gen_linha(nome_arq):
    with open(nome_arq, 'r') as arquivo:
        for i,linha in enumerate(arquivo.readlines()):
            if i >= 4:
                yield linha.strip().split('","')

dados = gen_linha("dados.csv")
print(os.chdir("maluquicie"))
print(os.getcwd())

print(next(dados))

# if __name__ == "__main__":
#     nome_arq = "dados.csv"

#     for linha in converte_linha(nome_arq):
#         print(linha)
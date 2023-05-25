import os
import sys

def gen_linha(nome_arq):
    with open(nome_arq, 'r') as arquivo:
        for i,linha in enumerate(arquivo.readlines()):
            if i >= 4:
                yield linha.strip().split('","')

def converte_linha(nome_arq):

    for linha in gen_linha(nome_arq):
        linha_convertida = []
        for coluna in linha:
            try:
                f = float(coluna)
                if int(f) == f:
                    linha_convertida.append(int(f))
                else:
                    linha_convertida.append(f)
            except ValueError:
                linha_convertida.append(coluna)
        yield linha_convertida

dados = gen_linha("dados.csv")
os.chdir("maluquicie")

if __name__ == "__main__":
    nome_arq = "dados.csv"

    lista_linhas = []

    for linha in converte_linha(nome_arq):
        lista_linhas.append(linha)

    print(f"São {len(linha)} linhas")
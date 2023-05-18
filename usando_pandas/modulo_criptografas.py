import string

dicionario = string.ascii_uppercase + string.ascii_lowercase + " !?.,"

def cifra_reversa(mensagem) -> str:
    resultado = ""
    caracteres_restantes = len(mensagem) - 1

    while caracteres_restantes >= 0:
        resultado = resultado + mensagem[caracteres_restantes]
        
        caracteres_restantes -= 1

    return resultado

def cifra_de_cesar(mensagem, modo, chave = 3) -> str:
    resultado = ""

    for caractere in mensagem:
        if caractere in dicionario:
            indice_caractere = dicionario.find(caractere)
            indice_corrigido = 0

            if modo == "encriptar":
                indice_corrigido = indice_caractere + chave
            elif modo == "decriptar":
                indice_corrigido = indice_caractere - chave
            
            tamanho_dicionario = len(dicionario)

            if indice_corrigido > tamanho_dicionario:
                indice_corrigido = indice_corrigido - tamanho_dicionario
            if indice_corrigido < 0:
                indice_corrigido = indice_corrigido + tamanho_dicionario
            
            resultado = resultado + dicionario[indice_corrigido]

        else:
            resultado = resultado + caractere

    return resultado


print(dicionario)
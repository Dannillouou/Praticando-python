# import para manipular arquivos
import os

def rodandoArquivos():
    # brincando com arquivos
    try: # tenta executar
        # Tratamento de exceção é uma boa prática, pois nem sempre a
        # abertura de arquivos pode funcionar
        
        # abrindo arquivo - retorna um objeto de arquivo
        # padrão read - r
        # modos: r - leitura, w - escrita, a - append
        arquivo = open("coltec.txt", "r")

        conteudo = arquivo.read(6)
        print(conteudo)

        maisConteudo = arquivo.read(5)
        print(maisConteudo)
    finally: # sempre é executado no fim
        arquivo.close

    with open("coltecEscreve.txt", "w") as coltec:
        # A função with faz o tratamento de exceção especificamente 
        # para arquivos abertos, fazendo o try e colocando o 
        # fechamento no finally
        
        coltec.write("Coltec!\n")
        coltec.write("ELITEEEE")

    with open("coltecEscreve.txt", "r+") as coltec:
        # A função with faz o tratamento de exceção especificamente 
        # para arquivos abertos, fazendo o try e colocando o 
        # fechamento no finally
        
        mensagem = input("O que você tem a dizer sobre o coltec? ")
        coltec.write("\n\nMensagem para o coltec do usuário:")
        coltec.write("\n" + mensagem)

        # voltando para o começo do arquivo para poder lê-lo:
        arquivo.seek(0)
        
        linhas = coltec.readlines()
        # recupera lista com todas as linhas
        print(linhas)

        # de novo...
        arquivo.seek(0)
        
        # Printando lista de linhas no arquivo
        linhas.append("Desculpa repeti a mensagem tava muito emocionado e com sono, nem vi")
        coltec.writelines(linhas)

    # Manipulando diretórios
    # change directory
    os.chdir('c:\\Users\B51995')
    diretorioAtual = os.getcwd()
    print(diretorioAtual)

    listaDiscoC = os.listdir('C:\\')
    print(listaDiscoC)

    os.chdir(diretorioAtual + '\Desktop')
    diretorioAtual = os.getcwd()
    print(diretorioAtual)
    caminho = diretorioAtual.split("\\")
    print(caminho)

    # voltando um diretório apagando a pasta mais à direita
    del caminho[-1]
    print(caminho)
    diretorioAtual = list(caminho)
    print(diretorioAtual)

    # voltando para a área de trabalho
    # mudando para string para usar no chdir
    print("andando por diretorios")
    diretorioAtual = '\\'.join(diretorioAtual)
    os.chdir(diretorioAtual + '\Desktop')
    diretorioAtual = os.getcwd()
    print(diretorioAtual)

    # criando diretorio
    print("criando diretorios")
    os.mkdir('teste')
    # mudando nome do diretorio
    os.rename('teste', 'novoDir')
    # indo para novo diretorio
    os.chdir('novoDir')
    diretorioAtual = os.getcwd()
    print(diretorioAtual)

    # abrindo arquivo agora no novo diretorio
    with open("testezin.txt", "w") as arquivo:
        arquivo.write('Arquivo novo p deletar fodas')

    # deletando arquivo
    input("Arquivo prestes a ser deletado")
    os.remove("testezin.txt")
    print("Arquivo deletado \n")

    # voltando um diretorio para apagar o diretorio agora vazio
    # primeiro, transforma o caminho em uma lista com as pastas usando o separador \
    caminho = diretorioAtual.split("\\")
    # deleta a pasta mais profunda da lista
    del caminho[-1]
    # pega a lista e transforma novamente em string, separando com a "\", 
    # o próprio caractere de separação de pastas
    diretorioAtual = '\\'.join(caminho)
    # muda o funcionamento do programa para o diretorio atual
    os.chdir(diretorioAtual)
    print(diretorioAtual)

    # deletando diretório vazio
    print("diretorio vazio prestes a ser deletado")
    os.rmdir("novoDir")
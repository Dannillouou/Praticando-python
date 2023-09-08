def rodandoNaoLocal():
    #Variável não-local

    #função de fora 
    def fora():
        message = 'local'

        #função de dentro  
        def dentro():
            #variável não-local
            nonlocal message

            message = 'não-local'
            print("drento:", message)

        dentro()
        print("fora:", message)

    fora()
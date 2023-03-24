#importando outro module
import variables

def rodandoIO():
    #Input e output na cobrinha

    #print "avançado"
    #sep padrão= ' '
    #end padrão= '\n'
    print('printizinho de cria', 2023, 'muito foda', variables.hello, sep=',', end='\n\n')
    print('printizinho de cria', 2023, 'muito foda e esse sem end', variables.hello, sep=', ')
    print('printizinho de cria sem sep', 2023, 'muito foda', variables.hello,)

    #input
    receber = input('Digite algo: ')
    print(receber)

    try:
        idade = int(input("Digte sua idade"))
        print(f"Voce tem {idade} anos")
    except:
        print("C é burro? Eu pedi um número porra")

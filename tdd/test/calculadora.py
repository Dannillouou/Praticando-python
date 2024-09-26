""" Módulo: Calculadora de Soma. """

def soma (numero, *args):
    if args:
        return numero + sum(args)
    else:
        return numero

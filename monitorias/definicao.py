"""
classe aluno com propridades:
- nome
- matricula
- bolsista
- curso
- notas
- cr

com métodos:
- get_nome
- get_matricula
- set_cr (oculto)
- adicionar_notas
- calcular_cr
"""

matriculas = [0]

class Aluno():

    def __init__(self, nome, curso, bolsa) -> None:
        self.__nome = nome
        self.__matricula = matriculas[-1] + 1
        matriculas.append(self.__matricula)

        self.__curso = curso
        self.__bolsista = bolsa

        self.__notas = None
        self.__cr = None

    @property
    def nome(self):
        print("Oh o nome aí")
        return self.__nome
    
    @property
    def matricula(self):
        return self.__matricula
    
    @property
    def cr(self):
        return self.__cr
    
    @property
    def curso(self):
        return self.__curso
    
    @curso.setter
    def curso(self, curso_novo):
        # exemplo de tratamento:
        # if curso_novo not in banco_de_dados:
        #   print("nao tem")
        #   return
        
        self.__curso = curso_novo

    

    
        


# Identacao: 4 espaços

# Separamos argumentos do corpo da funcao com o dobro da indentação
# para os argumentos. Muitos argumentos em um nome longo devem ser
# separados em multiplas linhas, começando depois do nome da função
def funcao_com_nome_longo(
        argumento1, argumento2, 
        argumento3, argumento4):
    argumento3 = argumento1 + argumento2
    return argumento3

#=============================================================
isso_eh_uma_coisa = True
isso_eh_outra_coisa = True

# indentação de if's
if (isso_eh_uma_coisa 
        and isso_eh_outra_coisa):
    print(isso_eh_uma_coisa)

#=============================================================
# indentacao de construtores
lista = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]

#=============================================================
"""
Cada linha deve ter no máximo 79 caracteres.
Com comentários e documentação a 72 
Configuração no visual studio code:
"editor.rulers": [
        80
    ]
"""

#=============================================================
# em expressões muito longas de abertura de arquivos, podemos usar uma
# barra para separar as diferentes expressões
with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())

#=============================================================
# para vários operadores matemáticos de uma vez
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)

#=============================================================
# blank lines

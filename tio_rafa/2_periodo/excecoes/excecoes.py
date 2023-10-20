# quando queremos rodar um código potencialmente
# perigoso usamos o try para tentar rodar o código
# e tomar as deivdas medidas no caso do levantamento
# de exceção
# x = 10
# y = 0

# try:
#     resultado = x/y
    
#     # criando exceção manualmente
#     raise AssertionError
# except NameError:
#     print("Variável não existe!")
# except ArithmeticError:
#     # podemos usar super classes de exceção para tratar diversas exceções
#     # semelhantes de uma vez
#     print("Não é possível dividir por 0!")
# except:
#     print("Exceção levantada")

try:
    resultado = 10/0
except (ZeroDivisionError, OverflowError) as erro:
    print("Variavel não existe", erro)
except Exception:
    print("Não é possível realizar a divisão")
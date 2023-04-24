# exceções são problemas que são identificados após a fase de análise
# sintática do código, causados por erros lógicos, como tentar fazer
# uma operação imposível ou abrir um arquivo que não existe, por exemplo

# arquivo com exceções já inclusas no python
print(dir(locals()['__builtins__']))

# existem erros e exceções erros estão além do controle do programador
# e não deveríamos tentar lidar com eles. Excecões podem ser pegas e
# para que possamos lidar com elas

# Erro definido por mim que herda a classe Exception
class ErroIdadeInvalida(Exception):
    "Lançado quando o valor de input é menor do que 18"
    pass

maioridade = 18

# bloco para "testar" codigo e ficar pronto para fazer algo se uma exceção for lançanda
try:
    input_idade = int(input("Qual sua idade? "))
    # se input for menor do que a maioridade, lança a exceção
    if input_idade < maioridade:
        raise ErroIdadeInvalida
    # quando a exceção ocorre o resto do código dentro do try não é interpretado
    else:
        print("pode vota")

# se a exceção for lançada
except ErroIdadeInvalida:
    print("Exceção: input invalido")

# classe para lançar exceção para salario fora do intervalo
class SalarioForaIntervaloErro(Exception):
    """Exceção levantada para erros no input de salario

    Atributos: 
        salario -- input de salario que causou o erro
        mensagem -- explicacao para o erro
    """
    
    # sobrescrevendo o construtor de exception
    def __init__(self, salario, mensagem="Salary não está no range de (5000, 15000)"):
        # salario fica salvo para uso posterior
        self.salario = salario
        self.mensagem = mensagem
        # provavelmente isso busca na classe mãe o message e o sobrescreve, que vai ser
        # impresso quando a exceção for lançada
        super().__init__(self.message)

minimo_salario = 5000
maximo_salario = 15000
input_salario = int(input("Qual o seu salario? "))

if not minimo_salario < input_salario < maximo_salario:
    raise SalarioForaIntervaloErro(input_salario)
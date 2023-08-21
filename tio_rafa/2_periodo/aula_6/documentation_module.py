"""Documentação do módulo(resumo do módulo)

Diferença comentário x documentação:
comentário: explicação do código ao longo do mesmo
documentação: descrição sobre o funcionamento do código

Importante na escolha da forma de documentar o código:
ter um padrão (ÚNICO dentro do código) que seja aceito
pelo leitor de documentação
"""

# forma pior de documentar

# Função que calcula montante e juros em um regime
# de juros simples
# Type Hint: MyPy
def juros_simples(capital: int, taxa: int, tempo: int) -> tuple:
    juros = capital * (taxa / 100) * tempo
    montante = capital + juros

    # TODO: alterar estrutura de dados de retorno para lista
    # TODO: limitar montante e capital a dois dígitos decimais
    return(montante, juros)

def juros_compostos(capital, taxa, tempo) -> tuple:
    """Cálculo de Juros Compostos
    Parameters
    ----------
    capital: int
        blá-blá-blá
    taxa: int
        blá-blá-blá
    tempo: int
        blá-blá-blá

    Returns
    -------
    tuple
        blá-blá-blá
    """

    # forma melhor de documentar

    montante = capital * (pow((1 + taxa / 100), tempo))
    juros = montante - capital

    return (montante, capital)
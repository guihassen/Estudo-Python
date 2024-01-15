# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def multiplicacao_2 (numero):
    multiplicacao = numero *2
    return multiplicacao

def multiplicacao_3 (numero):
    multiplicacao = numero * 3
    return multiplicacao

def multiplicacao_4 (numero):
    multiplicacao = numero * 4
    return multiplicacao

vezes_2 = multiplicacao_2(4)
vezes_3 = multiplicacao_3(4)
vezes_4 = multiplicacao_4(4)

print(f"O numero vezes 2 é {vezes_2}, por 3 é {vezes_3}, por 4 é {vezes_4}")
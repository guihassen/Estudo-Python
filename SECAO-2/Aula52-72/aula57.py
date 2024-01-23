# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicacao(*args):
    total = 1
    for numeros in args :
        total *= numeros
    return total 
    

multiplicar = multiplicacao(6,5)
print(multiplicar)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(numero):
    num_par = numero /2 == 0
    if num_par :
        return(f"{numero} é par!")
    else :
        return(f"{numero} é impar!")
    

numero_par = par_impar(7)
print(numero_par)
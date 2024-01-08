"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

#Programa 2

entrada = input("Digite um horario: ")

try:
    horario = int(entrada)

    if horario >= 0 and horario <= 11 :
        print("Bom Dia !")
    
    elif horario >= 12 and horario <= 17 :
        print("Boa Tarde!")
    
    elif horario >= 18 and horario <= 23 :
        print("Boa Noite!")
    
    else: 
        print("Digite um horario correto!")
        
except :
    print("Apenas Numeros inteiros !")


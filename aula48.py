# EXERCICIO DO CPF (PRIMEIRO DIGITO)

"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""


cpf = '67347999057'
cpf_lista = cpf[:9]
contador = 10
resultado = 0

for digito in cpf_lista :
    resultado += int(digito) * contador
    contador -= 1     
digito_1 = (resultado*10) %11

if digito_1 <= 9 :
    print("O seu digito é:",digito_1)

else :
    print("Seu digito é 0")



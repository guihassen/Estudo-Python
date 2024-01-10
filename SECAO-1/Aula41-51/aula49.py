"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0

"""
#CALCULO PRIMEIRO DIGITO

cpf = '70184174066'
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

#CALCULO SEGUNDO DIGITO
cpf_lista_2 = cpf_lista + str(digito_1)
contador_2 = 11 
resultado_2 = 0

for digito in cpf_lista_2 :
    resultado_2 += int(digito) * contador_2
    contador_2 -= 1     
digito_2 = (resultado_2*10) %11

if digito_2 <= 9 :
    print("O segundo digito é:",digito_2)

else :
    print("O segundo digito é: 0")

novo_cpf = f"{cpf_lista}{digito_1}{digito_2}"
print(novo_cpf)

if novo_cpf == cpf :
    print("CPF VALIDO")

else :
    print("CPF INVALIDO")
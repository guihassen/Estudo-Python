# if/ elif/ else
# se/ se nao se/ se nao

#EXERCICIO CALCULO DE IMC

altura = float(input("Digite sua altura : "))
peso = float(input("Digite seu peso: "))
imc = peso / altura ** 2

if imc >= 30:
    print(f"Seu imc é {imc} e tu ta gigante! ")

elif imc <= 25 :
    print(f"Seu imc é {imc} e você ta razoavel !")

elif imc <= 20 :
    print(f"Seu imc é {imc} e tu ta fininho! ")

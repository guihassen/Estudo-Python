# EXERCICIO IF/ELIF/ELSE PT 2

numero_1  = int(input("Digite um numero: "))
numero_2 = int(input("Digite outro numero: "))

if numero_1 > numero_2 :
    print(f"o primeiro numero: {numero_1} é maior que o segundo numero: {numero_2}")
elif numero_2 > numero_1 :
    print(f"o segundo numero: {numero_2} é maior que o primeiro numero: {numero_1}")
elif numero_1 == numero_2 :
    print("Os numeros são iguais")

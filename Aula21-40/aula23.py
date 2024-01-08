#introdução ao try/except

numero_digitado = input("Digite um numero: ")

try:
    numero_float = float(numero_digitado)
    print(f"O dobro do seu numero é {numero_float * 2}")

except:
    print("Isso não é um numero! ")
    
# Uso do operador or

entrada = input("Digite [E] para Entrar ou [S] para sair: ")
senha_permitida = "Fofogui"

if entrada == "S" or entrada == "s" :
    print("Tchau coisa ruim!")

elif entrada == "E" or entrada ==  "e" :
    senha_digitada = input("Digite sua senha: ")

if senha_digitada == senha_permitida :
    print("Seja Bem-Vindo Mardito!")

elif senha_digitada != senha_permitida :
    print("Senha Incorreta, Mongol!")



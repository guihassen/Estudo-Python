#Uso do operador while e break

senha_digitada = input("Digite sua senha: ")
senha_permitida = "Guilerme"

while senha_permitida != senha_digitada :
    senha_digitada = input("Senha Incorreta, Digite novamente: ")

    if senha_digitada == senha_permitida :
        print("Bem-Vindo!")
        break
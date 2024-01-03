# uso de while e break

senha_permitida = "Guilerme"
senha_digitada = input("Digite sua senha: ")
login = senha_digitada == senha_permitida

while login == False :
    senha_digitada = input("Senha Incorreta! Digite novamente: ")
    if senha_digitada == senha_permitida :
        print ("Bem Vindo !")
        break 
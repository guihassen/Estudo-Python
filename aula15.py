#USO DO COMANDO AND

entrada = input("[E]ntrar ou [S]air: ")
senha_permitida = "Guilerme"

if entrada == 'E' :
    senha_digitada = input("Digite sua senha: ")

if entrada == "E" and senha_digitada == senha_permitida :
    print("Bem vindo!")
elif entrada == "E" and senha_digitada != senha_permitida :
    print("Senha Incorreta! ")
elif entrada == "S" :
    print("Adeus!")
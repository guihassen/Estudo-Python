# EXERCICIO CALCULADORA


while True :
    opcao = input("Digite [E] para Entrar e [S] para Sair: ")
    entrada = opcao.startswith("E")
    
    while entrada :
        print("Bem vindo!")

        numero_1 = input("Digite um numero: ")
        numero_2 = input("Digite outro numero: ")
        operacao = input("Escolha entre +, -, / , * : ") 
        operador_permitido = "+ - / *"
       
        if numero_1.isdigit() and numero_2.isdigit() :
            numero_1_valido = float(numero_1)
            numero_2_valido = float(numero_2)

        else :
            print("Voce nao digitou um numero! ")   
            continue
       
        if operacao in operador_permitido and len(operacao) == 1 :
        
            if numero_1 and numero_2 and "+" in operacao :
                adicao = numero_1_valido + numero_2_valido
                print(adicao)
        
            elif numero_1_valido and numero_2 and "-" in operacao :
                subtracao = numero_1_valido - numero_2_valido
                print(subtracao)
        
            elif numero_1_valido and numero_2 and "/" in operacao :
                divisao = numero_1_valido / numero_2_valido
                print(divisao)

            elif numero_1_valido and numero_2 and "*" in operacao :
                multiplicacao = numero_1_valido * numero_2_valido
                print(multiplicacao)
        else :
            print("Digite apenas um operador!")
            continue
# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

for pergunta in perguntas :
    print(pergunta['Pergunta'])
    print()
    print(pergunta['Opções'])

    for opcao in pergunta['Opções'] :
        escolha = input("Escolha um numero:")
        escolha_int = int(escolha) 
        acerto = 0
        erro = 0

        if escolha in pergunta['Resposta']:
            print("\nCerto!\n")
            acerto += 1
            
        
        else :
            print("\nErrado!\n")
            erro += 1
        
        break


        
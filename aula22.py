# EXERCICIO
"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."

"""
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome and idade:
    print(f"Seu nome é: {nome}")
    print(f"Seu nome ao contrario é: {nome [::-1]}")
    numero_letras = len(nome)
    print(f"Seu nome tem {numero_letras} letras")
    print(f"A primeira letra do seu nome é: {nome[0]}")
    print(f"A ultima letra do seu nome é: {nome[4]}")

else :
    print("Desculpe, você deixou campos vazios.")
    
"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
letras_acertadas = ""
repeticoes = 0
palavra_secreta = "amigo"


while True:
    
    print("\nDescubra a palavra secreta, digitando uma letra por vez de A a Z ") 
    print("LEMBRETE: USE APENAS LETRAS MINUSCULAS!\n")
    letra_digitada = input("Digite uma letra: ")
    
    if len(letra_digitada) > 1 :
        print("Digite apenas uma letra por vez !")
        continue

    if letra_digitada in palavra_secreta :
        letras_acertadas += letra_digitada
               
    palavra_final = ""
    for letra_secreta in palavra_secreta :
         
         if letra_secreta in letras_acertadas :
              print(letra_secreta)
              palavra_final += letra_secreta 
        
         else :
              print("*")
              break
    
    if palavra_final == palavra_secreta :
         print("Parabéns!! VOCÊ GANHOU !!!")
         print("A palavra final era: ",palavra_secreta)
        
    
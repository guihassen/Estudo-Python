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
letras_secreta = ""
#palavra_secreta = "Amigo"

while True:
    print("Descubra a palavra secreta, digitando uma letra por vez de A a Z")
    letras_secreta = input("Digite a primeira letra: ")
    letras = letras.range("a,z")
    
    #for letras_corretas in 
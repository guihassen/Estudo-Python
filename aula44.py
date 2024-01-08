#EXERCICIO LISTA DE COMPRAS
import os

lista_mercado = []

while True:
  entrada =input("Selecione uma opção:\n [i]nserir [a]pagar [l]istar: ")
  
  if entrada == "i":   
    os.system("cls")
    item_adicionado = input("Digite o item que deseja adicionar: ")
    lista_mercado.append(item_adicionado)   
  
  if entrada == "a":
    os.system("cls")
    item_excluido = int(input("Escolha o indice a ser apagado: "))
    lista_mercado.pop(item_excluido)

  if entrada == "l" :
    
    if len(lista_mercado) == 0:
      print("Nada para listar!")

    for indice, item in enumerate(lista_mercado,start = 1) :
      print(indice,item)

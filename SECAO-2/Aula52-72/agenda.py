#EXERCICIO FAZER UMA AGENDA SIMPLES PARA PRATICAR DEF E DICT
import os 

tarefas = {
     'tarefa' : []
}    

def criar_tarefas() :
    tarefa = input("Digite a tarefa: ")
    adicionar_tarefa = tarefas['tarefa'].append(tarefa)
    os.system('cls')
    return adicionar_tarefa

def listar_tarefas () :
    for tarefas_listadas in tarefas['tarefa']:
        listar = print(tarefas_listadas)
    return listar

def apagar_tarefas():
    listar_tarefas()
    if tarefas['tarefa']:
        onde_apagar = input("Escolha a tarefa para apagar: ")
        if onde_apagar in tarefas['tarefa']:
            tarefas['tarefa'].remove(onde_apagar)


while True :  
    
    escolha = int(input("[1] para adicionar tarefa. \n[2] para listar. \n[3] para apagar. \nEscolha uma opcao: "))
    os.system('cls')
    if escolha == 1 :
        criar_tarefas()
        
    elif escolha == 2 :
         listar_tarefas()   

    elif escolha == 3 :
        apagar_tarefas()
    
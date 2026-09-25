# python3 lista-tarefas.py
# 1 - Mostrar tarefas
# 2 - Mostrar tarefas concluidas
# 3 - Mostrar tarefas não concluidas
# 4 - Mostrar tarefas por prioridade
# 5 - Cadastrar tarefa nova
# 6 - Finalizar tarefa
# 7- Rmover tarefa
# 0 - Sair

tarefas = [
    {"titulo":"Lavar a louça", "concluida?":"sim", "prioridade":"baixa"},
    {"titulo":"Louvar Kasane Teto", "concluida?":"nao", "prioridade":"alta"},
    {"titulo":"arrumar o quarto", "concluida?":"sim", "prioridade":"media"}
]

def Mostrar_tarefas():
    print (tarefas)
def Tarefas_concluidas():
    for tarefa in tarefas:
        if tarefa["concluida?"] == "sim":
            print (tarefa)
def Tarefas_não_concluidas():
     for tarefa in tarefas:
        if tarefa["concluida?"] == "nao":
            print (tarefa)
def Tarefas_por_prioridade():
    for tarefa in tarefas:
        if tarefa["prioridade"] == "alta":
            print (tarefa)
    for tarefa in tarefas:
        if tarefa["prioridade"] == "media":
            print (tarefa)
    for tarefa in tarefas:
        if tarefa["prioridade"] == "baixa":
            print (tarefa)
def Cadastrar_tarefa():
    while True:
        print ("---> Cadastrar uma nova tarefa <---")
        titulo = input ("Digite um titulo da tarefa: ")
        concluida = "nao"
        prioridade_k = input ("Qual a prioridade da tarefa?: ")
        
        if prioridade_k == "alta":
            nova_tarefa = {
                "titulo": titulo,
                "concluida?": concluida,
                "prioridade": prioridade_k
            }
            tarefas.append(nova_tarefa)
            break
        elif prioridade_k == "media":
            nova_tarefa = {
                "titulo": titulo,
                "concluida?": concluida,
                "prioridade": prioridade_k
            }
            tarefas.append(nova_tarefa)
            break
        elif prioridade_k == "baixa":
            nova_tarefa = {
                "titulo": titulo,
                "concluida?": concluida,
                "prioridade": prioridade_k
            }
            tarefas.append(nova_tarefa)
            break
        else:
            print ("Informe uma prioridade válida (alta, media, baixa)")
def Finalizar_tarefa():
    indice = tarefas.index( (input("Qual tarefa deseja finalizar? ")))
    concluida_s = "sim"
    produtos[indice] =  {"concluida?": concluida_s,}

while True: 
    print (" ---> Lista de tarefas <--- ")
    print ("1 - Mostrar tarefas")
    print ("2 - Mostrar tarefas concluidas")
    print ("3 - Mostrar tarefas não concluidas")
    print ("4 - Mostrar tarefas por prioridade")
    print ("5 - Cadastrar nova tarefa")
    print ("6 - Finalizar tarefa")
    print ("0 - Sair")


    opcao = input ("Escolha uma opção: ")

    if opcao == "1":
        Mostrar_tarefas()
    elif opcao == "2":
        Tarefas_concluidas()
    elif opcao == "3":
        Tarefas_não_concluidas()
    elif opcao == "4":
        Tarefas_por_prioridade()
    elif opcao == "5":
        Cadastrar_tarefa()
    elif opcao == "6":
        Finalizar_tarefa()
    elif opcao == "0":
        print ("saindo do sistema...")
        break
    else:
        print ("ææææææææææææææææææææææææææææææææææææææææææææææææææææææææææææææææææææææææææææææææææææææææææææææææææææææææææææ")
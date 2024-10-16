class Tarefa:
    def __init__(self, nome, status) -> None:
        self.nome = nome
        self.status = status

tarefas = []

def exibirMenu():
    print("1 - Adicionar uma nova tarefa")
    print("2 - Listar todas as tarefas")
    print("3 - Marcar uma tafera como concluída")
    print("4 - Remover uma tarefa")
    print("5 - Sair do programa\n")

def adicionarTarefa():
    status = "Pendente"
    nome = input("Digite o nome da tarefa\n")
    print("Essa tafera foi concluída?")
    check_tarefa = int(input("1 - SIM ou 2 - NÃO\n"))
    if check_tarefa == 1:
        status = "Concluída"
    tarefa = Tarefa (nome, status) #criando a instância
    tarefas.append(tarefa) #adicionando a instância na  lista
    print("***Tarefa adicionada***\n")

def listarTarefa():
    print("***** Tarefas cadastradas *****\n")
    for i, tarefa in enumerate(tarefas):
        print("Nome: ", tarefa.nome) 
        print("Status: ", tarefa.status)
        print(f"Índice: {i}\n")

def marcarTarefaConcluida():
        indice = int(input("Digite o índice: "))
        tarefa = tarefas[indice]
        status = "Concluída"
        nome = tarefa.nome
        tarefa = Tarefa (nome, status) #tirei o 1 do tarefa1
        tarefas[indice] = tarefa
        print(f"***Tarefa {tarefa.nome} concluída***\n")

def removerTarefa(): #como crio uma instancia dentro dessa função? / para acessar o objeto preciso de criar instancia? *ele já está dentro do vetor*
    indice = int(input("Digite o índice: "))
    tarefas.pop(indice) #o .pop tb serve para transferir os dados de uma lista para uma variavel
    print("***Tarefa deletada***\n")
    #print(f"***Tarefa {tarefa.nome} deletada***\n")

while (True):

    exibirMenu()
    opcao_menu = int(input("Informe a opção desejada: \n"))

    if (opcao_menu == 1):
        adicionarTarefa()
    
    elif (opcao_menu == 2):
        listarTarefa()

    elif (opcao_menu == 3):
        marcarTarefaConcluida()
    
    elif (opcao_menu == 4):
        removerTarefa()

    elif (opcao_menu == 5):
        break

print("Fim do programa")
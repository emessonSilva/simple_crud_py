'''
Sistema de Cadastro de tarefas, ou algum projeto que te motive - entrega dia 10/07
Você está desenvolvendo um sistema de cadastro simples em Python. O programa deve permitir ao
usuário realizar as seguintes operações através de um menu interativo:
1. Cadastrar uma tarefa: O usuário poderá cadastrar uma nova tarefa no sistema.
2. Alterar uma tarefa: O usuário poderá alterar informações de uma tarefa existente no sistema.
3. Excluir uma tarefa: O usuário poderá excluir uma tarefa do sistema.
4. Listar tarefas: O usuário poderá visualizar a lista de todas as tarefas cadastrados.
5. Sair do sistema: Encerra a execução do programa.
Funcionamento do Programa
• Cadastro da tarefa: O usuário será solicitado a inserir informações para cadastrar uma nova
tarefa. Essas informações podem variar dependendo do tipo de dados que você está
gerenciando (ex: descrição, etc.).
• Alteração da tarefa: O usuário poderá selecionar uma tarefa existente na lista e alterar uma
ou mais informações associadas a essa tarefa.
• Exclusão da tarefa: O usuário poderá selecionar uma tarefa existente na lista e removê-lo
do sistema.
• Listagem de tarefas: Todos as tarefas cadastradas devem ser exibidos de maneira formatada
para o usuário.
• Sair do Sistema: Quando o usuário escolher essa opção, o programa deve encerrar sua
execução.
Requisitos Técnicos
• Utilize estruturas de repetição para permitir que o usuário realize múltiplas operações sem
precisar reiniciar o programa.
• Use coleções em Python para armazenar e gerenciar os itens cadastrados.
• Garanta que o menu de opções seja exibido após cada operação, até que o usuário decida
sair.
Exemplo de Menu
=== Menu ===
1. Cadastrar uma tarefa
2. Alterar uma tarefa
3. Excluir uma tarefa
4. Listar tarefas
5. Sair do sistema
Escolha uma opção:
'''

tasks = []

def show_menu():
    print("=== Menu ===")
    print("1. Cadastrar uma tarefa")
    print("2. Alterar uma tarefa")
    print("3. Excluir uma tarefa")
    print("4. Listar tarefas")
    print("5. Sair do sistema")
    return input("Escolha uma opção: ")

def create_task():
    print()
    description = input("Digite a descrição da tarefa: ")
    tasks.append(description)
    print()
    print("Tarefa cadastrada com sucesso!")
    print()

def update_task():
    print()
    read_task()
    index = int(input("Digite o número da tarefa que deseja alterar: ")) - 1
    if 0 <= index < len(tasks):
        new_description = input("Digite a nova descrição da tarefa: ")
        tasks[index] = new_description
        print()
        print("Tarefa alterada com sucesso!")
        print()
    else:
        print("Número de tarefa inválido.")
        print()

def delete_task():
    read_task()
    index = int(input("Digite o número da tarefa que deseja excluir: ")) - 1
    if 0 <= index < len(tasks):
        tasks.pop(index)
        print()
        print("Tarefa excluída com sucesso!")
        print()
    else:
        print("Número de tarefa inválido.")
        print()

def read_task():
    if not tasks:
        print("Nenhuma tarefa cadastrada.")
    else:
        for i, task in enumerate(tasks, start=1):
            print()
            print('Tarefas Cadastradas:')
            print()
            print(f"{i}. {task}")
            print()

def main():
    while True:
        option = show_menu()
        if option == '1':
            create_task()
        elif option == '2':
            update_task()
        elif option == '3':
            delete_task()
        elif option == '4':
            read_task()
        elif option == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, por favor tente novamente.")

main()


# adicionar, remover, refazer
modify = 'a'
todo_list = []

def modify_global(value):
    global modify
    modify = value

def show_todo(todo_list):
    for x in range(len(todo_list)):
        print(f'{x+1} - {todo_list[x]}')

def add_todo(todo_list):
    add_ask = input('Nova tarefa: ')

    modify_global(add_ask)  # guarda a modificacao

    todo_list.append(add_ask)  #adiciona a tarefa na lista
    print('Tarefa adicionada.')


def remove_todo(todo_list):
    show_todo(todo_list)
    remove_ask = int(input('Número da tarefa que deseja remover: '))

    modify_global(todo_list[remove_ask-1])

    todo_list.pop(remove_ask-1)  #remove a tarefa desejada
    print('Tarefa removida.')

def modify_todo(todo_list):

    if modify in todo_list:
        todo_list.remove(modify)  #remove o ultimo valor adicionado
    else:
        todo_list.append(modify)  #adiciona o ultimo valor removido

if __name__ == "__main__":

    menu = 'Digite 0 para finalizar.\n(1) Nova Tarefa\n(2) Remover tarefa\n(3) Desfazer última alteração\n(4) Listar as tarefas\nEscolha: '

    while True:

        ask = int(input(menu))  #imprime a variavel menu e recebe a opção desejada pelo usuario

        if ask == 1:
            add_todo(todo_list)

        elif ask == 2:
            remove_todo(todo_list)

        elif ask == 3:
            modify_todo(todo_list)

        elif ask == 4:
            show_todo(todo_list)
        else:
            break



# adicionar, remover, refazer

def listar(a):
    for x in range(len(a)):
        print(f'{x+1} - {a[x]}')

if __name__ == "__main__":
    lista_tarefas = []
    modificacao = ''

    menu = '(1) Nova Tarefa\n(2) Remover tarefa\n(3) Desfazer última alteração\n(4) Listar as tarefas\nEscolha: '

    while True:

        opcao = int(input(menu))  #imprime a variavel menu e recebe a opção desejada pelo usuario

        if opcao == 1:
            opcao2 = input('Nova tarefa: ')
            modificacao = opcao2  #salva a nova tarefa para uma futura modificacao
            lista_tarefas.append(opcao2)  #insere uma nova tarefa
            print('Tarefa adicionada.')

        elif opcao == 2:
            listar(lista_tarefas)
            opcao2 = int(input('Qual tarefa deseja remover:  '))
            modificacao = lista_tarefas[opcao2-1]  #salva a tarefa removida para uma futura modificacao
            lista_tarefas.pop(opcao2-1)   #exclui a tarefa removida
            print('Tarefa excluida.')

        elif opcao == 3:
            if modificacao in lista_tarefas:
                lista_tarefas.remove(modificacao)  #remove o ultimo valor adicionado
            else:
                lista_tarefas.append(modificacao)   #insere o ultimo valor removido

        else:
            print('*'*20)
            listar(lista_tarefas)
            print('*' * 20)




def listar(lista):
    if not lista:
        print('Você ainda não fez uma lista')
        return
    print('\nLista de Tarefas:')
    for i,v in enumerate(lista, start=1):
        print(f'\t{i}. {v}')
    print()

def desfazer(lista):
    if not lista:
        print('Nada a desfazer!')
        return

    recebe = lista.pop()
    lista_def.append(recebe)

def refazer(lista):
    if not lista_def:
        print('Nada a refazer!')
        return

    recebe = lista_def.pop()
    lista.append(recebe)


lista_de_tarefas = []
lista_def = []

while True:
    tarefa = input('Digite uma tarefa ou list(para listar as tarefas), def(para desfazer a ultima tarefa, ref(para refazer a ultima tarefa) ou exit para sair: ').lower()

    if tarefa == 'list':
        listar(lista_de_tarefas)
        continue
    elif tarefa == 'def':
        desfazer(lista_de_tarefas)
        continue
    elif tarefa == 'ref':
        refazer(lista_de_tarefas)
        continue
    elif tarefa == 'exit':
        break

    lista_de_tarefas.append(tarefa)
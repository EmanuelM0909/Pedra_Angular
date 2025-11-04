#altere-o de forma a considerar operação como uma strig.
#ex.>>> FFFAAAS significa 3 chegadas de novos clientes, 3 atendimentos e o fim do programa.

ultimo = 10
fila = list(range(1, ultimo + 1))
while True:
    print(f'\nExistem {len(fila)} clientes na fila')
    print(f'Fila atual: {fila}')
    print('Digite "F" para add um novo cliente.')
    print('Digite "A" para atender.')
    print('Digite "S" para sair.')
    op = str(input('Operação (F, A ou S)')).upper().strip()
    cont = 0
    sair = False
    while cont < len(op):
        if op[cont] == 'A':
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f'Cliente {atendido} atendido!')
            else:
                print('Fila vazia! Ninguém para ser atendido.')
        elif op[cont] == 'F':
            ultimo += 1
            fila.append(ultimo)
        elif op[cont] == 'S':
            sair = True
            break
        else:
            print('Operação invalida! Tente novamente.')
        cont += 1
    if sair:
        break

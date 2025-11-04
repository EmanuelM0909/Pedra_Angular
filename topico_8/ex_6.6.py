ultimo = 0
fila_1 = []
fila_2 = []

while True:
    print(f'\nExistem {len(fila_1)} clientes na fila 1 e {len(fila_2)} na fila 2.')
    print(f'Fila 1 atual: {fila_1}')
    print(f'Fila 2 atual: {fila_2}')
    print('Digite F para adicionar um cliente ao fim da fila 1 (ou G para fila 2),')
    print('ou A para realizar o atendimento na fila 1 (ou B para fila 2)')
    print('S para sair.')

    operacao = input("Operação (F, G, A, B ou S): ").upper().strip()
    cont = 0
    sair = False

    while cont < len(operacao):
        # Define qual fila usar
        if operacao[cont] == 'F' or operacao[cont] == 'A':
            fila = fila_1
        else:
            fila = fila_2

        # Adicionar cliente
        if operacao[cont] == 'F' or operacao[cont] == 'G':
            ultimo += 1
            fila.append(ultimo)

        # Atender cliente
        elif operacao[cont] == 'A' or operacao[cont] == 'B':
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f'Cliente {atendido} atendido!')
            else:
                print('Fila vazia! Ninguém para atender.')

        # Sair do programa
        elif operacao[cont] == 'S':
            sair = True
            break

        # Operação inválida
        else:
            print(f'Operação inválida: {operacao[cont]} na posição {cont}.')

        cont += 1

    if sair:
        break

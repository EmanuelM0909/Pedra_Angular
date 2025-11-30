print('=== Sistema de Salas de Cinema — Modo Fox ===')

lugares_vagos = [10, 2, 1, 3, 0]
vendas = [0, 0, 0, 0, 0]

while True:
    sala = int(input('\nSala desejada (0 para sair): '))

    if sala == 0:
        print('\nEncerrando...')
        break

    # Verifica se a sala existe
    if sala < 1 or sala > len(lugares_vagos):
        print('Sala inválida!')
        continue

    indice = sala - 1   # Ajuste para índice da lista

    # Verifica se há vagas
    if lugares_vagos[indice] == 0:
        print('Desculpe, a sala está lotada!')
        continue

    # Pergunta os lugares desejados
    lugares = int(input(
        f'Quantos lugares você deseja? ({lugares_vagos[indice]} disponíveis): '
    ))

    # Verificações
    if lugares < 0:
        print('Número inválido!')
    elif lugares > lugares_vagos[indice]:
        print('Quantidade não disponível!')
    else:
        # Desconta e registra a venda
        lugares_vagos[indice] -= lugares
        vendas[indice] += lugares
        print(f'{lugares} lugar(es) vendido(s) com sucesso!')

# ------------------------- RESULTADOS FINAIS -------------------------

print('\n=== Relatório Final ===')

for i, vagos in enumerate(lugares_vagos):
    print(f'\nSala {i + 1}:')
    print(f' • Lugares vazios: {vagos}')
    print(f' • Lugares vendidos: {vendas[i]}')

print('\nObrigado por usar o sistema!')

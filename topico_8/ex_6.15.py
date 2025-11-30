print('=== Sistema de Salas de Cinema — Modo Fox ===')

# ----------------------------------------------------
# 1) Perguntar quantas salas existem
# ----------------------------------------------------
qtd_salas = int(input('Quantas salas o cinema possui? '))

# Criar listas vazias
lugares_vagos = []
vendas = []

# ----------------------------------------------------
# 2) Perguntar quantos lugares cada sala tem
# ----------------------------------------------------
for i in range(qtd_salas):
    lugares = int(input(f'Quantos lugares tem a sala {i+1}? '))
    lugares_vagos.append(lugares)
    vendas.append(0)  # No início, ninguém comprou nada

# ----------------------------------------------------
# 3) Sistema de vendas
# ----------------------------------------------------
while True:
    sala = int(input('\nSala desejada (0 para sair): '))

    if sala == 0:
        print('\nEncerrando...')
        break

    # Verifica se a sala existe
    if sala < 1 or sala > len(lugares_vagos):
        print('Sala inválida!')
        continue

    indice = sala - 1

    # Verifica se há vagas
    if lugares_vagos[indice] == 0:
        print('Desculpe, a sala está lotada!')
        continue

    lugares = int(input(
        f'Quantos lugares você deseja? ({lugares_vagos[indice]} disponíveis): '
    ))

    # Verificações
    if lugares < 0:
        print('Número inválido!')
    elif lugares > lugares_vagos[indice]:
        print('Quantidade não disponível!')
    else:
        lugares_vagos[indice] -= lugares
        vendas[indice] += lugares
        print(f'{lugares} lugar(es) vendido(s) com sucesso!')

# ----------------------------------------------------
# 4) Relatório Final
# ----------------------------------------------------
print('\n=== Relatório Final ===')

for i, vagos in enumerate(lugares_vagos):
    print(f'\nSala {i + 1}:')
    print(f' • Lugares vazios: {vagos}')
    print(f' • Lugares vendidos: {vendas[i]}')

print('\nObrigado por usar o sistema!')

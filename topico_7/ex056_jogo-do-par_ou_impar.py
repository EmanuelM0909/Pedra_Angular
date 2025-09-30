from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = computador + jogador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/Í] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e computador {computador}. Total de {total}')
    print('Deu par' if total % 2 == 0 else 'Deu ímpar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu!!!')
            v += 1
        else:
            print('Você Perdeu!!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!!!')
            v +=1
        else:
            print('Você perdeu!!!')
            break
    print('Vamos Jogar novamente!!!')
print(f'Você venceu com {v} vezes.')

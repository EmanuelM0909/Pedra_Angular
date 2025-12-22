from random import randint
from time import sleep

jogo = {}
print('Jogando os dados...\n')
sleep(1)

for jogador in range(1, 5):
    dado = randint(1, 6)
    jogo[f'Jogador {jogador}'] = dado
    print(f'Jogador {jogador} tirou {dado}')
    sleep(1)

print('\nRanking dos jogadores:')
ranking = sorted(jogo.items(), key=lambda item: item[1], reverse=True)

for posicao, jogador in enumerate(ranking):
    print(f'{posicao + 1}º lugar: {jogador[0]} com {jogador[1]}')

print(f'\n Vencedor: {ranking[0][0]} com {ranking[0][1]}!')


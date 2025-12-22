from random import randint
print('=' * 25)
print(f'Palpites Mega-Sena')
print('=' * 25)

l = []  # lista que guarda todos os jogos
tem = []  # lista temporária para cada jogo

qnt = int(input('Quantos jogos deseja gerar? '))

for i in range(qnt):
    tem.clear()  # limpa a lista antes de montar um novo jogo

    # monta 1 jogo com 6 números diferentes
    while len(tem) < 6:
        n = randint(1, 60)
        if n not in tem:  # impede números repetidos
            tem.append(n)

    tem.sort()  # deixa o jogo organizado em ordem crescente
    l.append(tem[:])  # salva uma cópia do jogo na lista principal

# mostra os jogos
print('-=' * 20)
for i, jogo in enumerate(l):
    print(f'Jogo {i + 1}: {jogo}')
print('-=' * 20)

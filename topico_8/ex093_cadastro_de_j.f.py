avaliacao_tec = dict()
avaliacao_tec['nome'] = str(input('Digite o nome do Jogador: '))
avaliacao_tec['quantidade'] = int(input(f'Quantas partidas {avaliacao_tec["nome"]} jogou: '))

gols = []
soma = 0
for c in range(avaliacao_tec['quantidade']):
     gols.append(int(input(f'Quantos gols na partida {c+1}: ')))
     soma += gols[c]
avaliacao_tec['gols'] = gols
avaliacao_tec['total'] = soma
print('-=' * 50)
print(avaliacao_tec)
print('-=' * 50)
for k, v in avaliacao_tec.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 50)
print(f'O jogador {avaliacao_tec["nome"]} jogou {avaliacao_tec["quantidade"]} jogos.')
for i, v in enumerate(avaliacao_tec['gols']):
    print(f'    => Na partida {i+1} fez {v} gols.')

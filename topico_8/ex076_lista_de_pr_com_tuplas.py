print('='*50)
print(f'{"LISTA DE PR COM TUPLAS":^40}')
print('='*50)
listagem = ('Lapís', 1.75,
            'Borracha', 2,
            'caderno', 15.90,
            'Estojo', 10.80,
            'Transferidor', 2.99,
            'Compasso', 9.99,
            'Mochila', 120.00,
            'Caneta', 2.00,
            'livro', 34.90,)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end=' ')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('='*50)

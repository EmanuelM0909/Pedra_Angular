from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10),
     randint(1, 10), randint(1, 10), )
print(f'Eu sorteia os valores', end=' ')
for c in num:
    print(f'{c}', end=' ')
print(f'\nO maior valor sorteado foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')

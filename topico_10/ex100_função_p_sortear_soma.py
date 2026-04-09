from random import randint
from time import sleep

def sorteia(lista):
    print("Sorteando 5 valores em um lista!")
    for cont in range(1, 5):
        n = randint(1, 5)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.3)

def soma_par(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')
num = list()
sorteia(num)
soma_par(num)
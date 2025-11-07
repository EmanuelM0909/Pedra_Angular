soma = cont = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma += n
        cont += 1
print(f'\nA soma de todos os {cont} de 3 de 1 à 500 foi {soma}')

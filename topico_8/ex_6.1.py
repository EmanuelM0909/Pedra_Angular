notas = [0, 0, 0, 0, 0, 0, 0]
soma = 0
cont = 0
while cont < 7:
    notas[cont] = float(input(f'Digite {cont}'))
    soma += notas[cont]
    cont += 1
cont = 0
while cont < 7:
    print(f'Nota {cont}: {notas[cont]:6.2f}')
    cont += 1
print(f'A média foi de {soma / cont:5.2f}')
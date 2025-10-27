'''notas = [6, 7, 5, 8, 9]
soma = 0
x = 0
while x < 5:
    soma += notas[x]
    x +=1
print(f'Média: {soma / x:5.2f}')'''
###
'''notas = [0, 0, 0, 0, 0]
soma = 0
x = 0
while x < 5:
    notas[x] = float(input(f'Nota {x}: '))
    soma += notas[x]
    x += 1
x = 0
while x < 5:
    print(f'Notas {x}: {notas[x]:6.2f}')
    x += 1
print(f'Média: {soma / x:5.2f}')'''
###                                                
'''num = [0, 0, 0, 0, 0]
cont = 0
while cont < 5:
    num[cont] = int(input(f'Número {cont +1}:'))
    cont += 1
while True:
    escolhido = int(input('Que posição você quer imprimir (0 para sair): '))
    if escolhido == 0:
        break
    else:
        print(f'Você escoçheu o número {num[escolhido - 1]}')'''
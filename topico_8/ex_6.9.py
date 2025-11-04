l = [15, 7, 27, 39, 1, 45, 66, 77, 887, 999]
p = int(input('Digite o primerio valor a procurar: (p)'))
v = int(input('Digite o segundo valor a procurar: (v)'))
cont = 0
achou_p = False
achou_v = False
primeiro = 0
while cont < len(l):
    if l[cont] == p:
        achou_p = True
        if not achou_v:
            primeiro = 1
    if l[cont] == v:
        achou_v = True
        if not achou_p:
            primeiro = 2
    cont += 1
if achou_p:
    print(f'{p} foi encontrado!')
else:
    print(f'{p} não foi encontrado!')
if achou_v:
    print(f'{v} foi encontrado!')
else:
    print(f'{v} não foi encontrado!')
if primeiro == 1:
    print(f'{p} foi o primeiro a ser encontrado.')
elif primeiro == 2:
    print(f'{v} foi o primeiro a ser encontrado.')


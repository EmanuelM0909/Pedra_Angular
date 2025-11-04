l = [15, 7, 27, 39, 1, 45, 66, 77, 887, 999]
p = int(input('Digite o primerio número para verificar: '))
v = int(input('Digite o segundo número  para verificar: '))
primeiro = cont = 0
achou_v = achou_p = False
posicao_p = posicao_v = 0
while cont < len(l):
    if l[cont] == p:
        achou_p = True
        posicao_p = cont
        if not achou_v:
            primeiro = 1
    if l[cont] == v:
        achou_v = True
        posicao_v = cont
        if not achou_p:
            primeiro = 2
    cont +=1
if achou_p:
    print(f'{p} foi encontrado na posição {posicao_p}!')
else:
    print(f'{p} não foi encontrado!')
if achou_v:
    print(f'{v} foi encontrado na posição {posicao_v}!')
else:
    print(f'{v} não foi encontrado!')
if primeiro == 1:
    print(f'{p} foi o primeiro a ser encontrado.')
elif primeiro == 2:
    print(f'{v} foi o primeiro a ser encontrado.')

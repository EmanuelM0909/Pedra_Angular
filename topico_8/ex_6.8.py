l = [15, 7, 27, 39]
print(l)
p = int(input('Digite o valor a procurar: '))
cont = 0
while cont < len(l) and l[cont] != p:
    cont += 1
if cont < len(l):
    print(f'{p} achado na posição {cont}')
else:
    print(f'{p} não encontrado')

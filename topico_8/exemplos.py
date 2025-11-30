###
"""notas = [6, 7, 5, 8, 9]
soma = 0
x = 0
while x < 5:
    soma += notas[x]
    x +=1
print(f'Média: {soma / x:5.2f}')"""
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
        print(f'Você escolheu o número {num[escolhido - 1]}')'''
###
'''l = [15, 7, 27, 39]
print(l)
p = int(input('Digite o valor a procurar '))
achou = False
cont = 0
while cont < len(l):
    if l[cont] == p:
        achou = True
        break
    cont += 1
if achou:
    print(f'{p} achado na posição {cont}')
else:
    print(f'{p} não foi achado')'''
###
'''l = [5, 9, 13]
for x, e in enumerate(l):
    print(f'[{x}] {e}')'''
###
'''compras = []
while True:
    produto = input('Produto: ')
    if produto == 'fim':
        break
    compras.append(produto)
for cont in compras:
    print(cont, end=' ')'''
###
'''l = ['maçãs', 'peras', 'kiwis']
for s in l:
    for letra in s:
        print(letra, end=' ')'''
###
'''p1 = ["maçã", 10, 0.30]
p2 = ["pera", 5, 0.75]
p3 = ["kiwi", 4, 0.98]

compras = [p1, p2, p3]

for e in compras:
    print(f'Produto: {e[0]}')
    print(f'Quantidade: {e[1]}')
    print(f'Preço: {e[2]:5.2f}')'''
###
'''compras = []
while True:
    produto = input('Produto: ')
    if produto == 'fim':
        break
    quantidade = int(input('Quantidade: '))
    preco = float(input('Preço: '))
    compras.append([produto, quantidade, preco])
soma = 0.0
for e in compras:
    print(f'{e[0]:2s} x {e[1]}un. -> R${e[2]:5.2f} = {e[1] * e[2]:6.2f}')
    soma += e[1] * e[2]
print(f'Total: "R$"{soma:7.2f}')'''
###
'''l = [7, 4, 3, 12, 8]
fim = 5
while fim > 1:
    trocou = False
    x = 0
    while x < (fim - 1):
        if l[x] > l[x + 1]:
            trocou = True
            temp = l[x]
            l[x] = l[x + 1]
            l[x +1] = temp
        x +=1
    if not trocou:
        break
    fim -= 1
for e in l:
    print(e)'''
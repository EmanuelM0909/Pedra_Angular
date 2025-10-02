totalc = mil = menor = cont = 0
barato = ' '
while True:
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$'))
    cont += 1
    totalc += preco  #a
    if preco > 1000:  #b
        mil += 1  #b
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar: [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra foi de {totalc:.2f}.')  #a
print(f'Temos {mil} produtos custando mais de R$1.000,00')  #b
print(f'O produto mais foi {barato} que custou {menor:.2f}')

print("Caixa registradora Fox")
print('Digite o código do produto e a quantidade.')
print('0 para sair')

total = 0.0

while True:

    cod = int(input('Digite o código do produto: '))
    preco = 0

    if cod == 0:
        break
    elif cod == 1:
        preco = 0.50
    elif cod == 2:
        preco = 1.00
    elif cod == 3:
        preco = 4.00
    elif cod == 5:
        preco = 7.00
    elif cod == 9:
        preco = 8.00
    else:
        print('Código invalido, tente novamente.')
    if preco != 0:
        quantidade = int(input('Digite a quantidade do produto: '))
        total = total + (quantidade * preco)
print(f'O total a pagar é de {total:.2f}')

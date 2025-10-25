cont = soma = 0
while True:
    num = int(input('Digite um número ("0" sai do programa): '))

    if num == 0:
        print('Fim do programa.')
        break
    else:
        soma += num
        cont += 1

if cont > 0:
    media = soma / cont
    print(f'A soma total foi de {soma}')
    print(f'A quantidade de números foi de {cont}')
    print(f'Média foi {media:.2f}')
else:
    print('Você não digitou nenhum número!')

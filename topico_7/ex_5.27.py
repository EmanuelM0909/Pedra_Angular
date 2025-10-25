num = int(input('Digite um número para verificar se é palíndromo: '))
if num < 0:
    print(f'O {num} é negativo, não é palíndromo.')
else:
    original = num
    invertido = 0

    while num > 0:
        resto = num % 10
        invertido = invertido * 10 + resto
        num //= 10

    if original == invertido:
        print('É palíndromo.')
    else:
        print('Não é palíndromo.')

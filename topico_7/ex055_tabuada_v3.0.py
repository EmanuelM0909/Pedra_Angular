while True:
    n = int(input('Digite um número positivo para fazer sua Tabuada: '))
    if n < 0:
        break
    x = 1
    while x <= 10:
        print(f'{n} x {x} = {n*x}')
        x = x + 1
print('Fim do Programa, tabuada finalizada!')

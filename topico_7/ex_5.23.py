numero = int(input('Digite um número para verificar se é primo: '))
if numero < 0:
    print("Número inválido. Digite apenas valores positivos")
if numero == 0 or numero == 1:
    print(f'{numero} por definição não é número primo.')
else:
    if numero == 2:
        print(f'{numero} é o unico número "par" que é primo.')
    elif numero % 2 == 0:
        print(f'{numero} não é primos pois, 2 é o único número par primo.')
    else:
        x = 3
        while x < numero:
            if numero % x == 0:
                break
            x += 2
        if x == numero:
            print(f'{numero} é primo')
        else:
            print(f'{numero} não é primo, pois é divisível por {x}')

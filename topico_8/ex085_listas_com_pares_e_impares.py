l = [[], []]
for cont in range(7):
    num = int(input(f'Digite o  valor {cont + 1}: '))
    if num % 2 == 0:
        l[0].append(num)
    else:
        l[1].append(num)
print('-=' * 30)
l[0].sort()
l[1].sort()
print(f'Os valores pares foram {l[0]}\nE os valores ímpares foi {l[1]}')

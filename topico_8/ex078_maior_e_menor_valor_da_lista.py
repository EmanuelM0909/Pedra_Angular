L = []
maior = 0
menor = 0
for c in range(0, 5):
    L.append(int(input(f"Digite um valor para a posição {c}: ")))
    if c == 0:
        maior = menor = L[c]
    else:
        if L[c] > maior:
            maior = L[c]
        if L[c] < menor:
            menor = L[c]

print(L)
print(f'O maior foi {maior} encontrado em ', end='')
for i, v in enumerate(L):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor foi {menor} encontrado em ', end='')
for i, v in enumerate(L):
    if v == menor:
        print(f'{i}...', end='')
print()

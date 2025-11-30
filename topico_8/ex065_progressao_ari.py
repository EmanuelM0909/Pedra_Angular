p1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = p1 + (10 - 1) * razao
for c in range(p1, decimo + razao, razao):
    print(f'{c} ->', end=' ')
print('Fim')
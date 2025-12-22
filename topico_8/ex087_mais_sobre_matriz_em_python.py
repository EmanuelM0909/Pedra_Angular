matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

soma_par = 0
soma_coluna = 0
maior_seg = 0

# ======== COLETAR VALORES ========
for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

print('-=' * 30)

# ======== MOSTRAR MATRIZ E SOMAR OS PAR ========
for linha in range(3):
    for coluna in range(3):
        valor = matriz[linha][coluna]
        print(f'[{valor:^5}]', end='')

        if valor % 2 == 0:
            soma_par += valor
    print()

print('-=' * 30)

print(f'A soma dos valores pares é {soma_par}')

# ======== SOMA DA TERCEIRA COLUNA ========
for linha in range(3):
    soma_coluna += matriz[linha][2]

print(f'A soma da terceira coluna é {soma_coluna}')

# ======== MAIOR VALOR DA SEGUNDA LINHA ========
maior_seg = matriz[1][0]   # começa assumindo o 1º valor da 2ª linha

for coluna in range(1, 3):  # analisa as colunas restantes da linha 1
    if matriz[1][coluna] > maior_seg:
        maior_seg = matriz[1][coluna]

print(f'O maior valor da segunda linha é {maior_seg}')

'''matriz = [
    [],  # linha 1
    [],  # linha 2
    [],  # linha 3
]

# Preencher a linha 1
for i in range(3):
    num = int(input(f'Digite um número para a posição [0, {i}]: '))
    matriz[0].append(num)

# Preencher a linha 2
for i in range(3):
    num = int(input(f'Digite um número para a posição [1, {i}]: '))
    matriz[1].append(num)

# Preencher a linha 3
for i in range(3):
    num = int(input(f'Digite um número para a posição [2, {i}]: '))
    matriz[2].append(num)

print('-=' * 30)

print(matriz)'''

###

'''matriz = [[], [], []]   # 3 linhas vazias

for linha in range(3):           # controla as linhas 0, 1 e 2
    for coluna in range(3):      # controla as colunas 0, 1 e 2
        valor = int(input(f'Digite um número para [{linha}, {coluna}]: '))
        matriz[linha].append(valor)'''

###

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para {linha}, {coluna}: '))
print('-=' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

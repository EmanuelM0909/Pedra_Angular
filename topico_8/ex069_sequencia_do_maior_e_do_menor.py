maior = 0
menor = 0

for c in range(1, 6):
    peso = float(input(f'Qual o peso do usuário {c}º: '))

    # Se for a primeira repetição, inicializa maior e menor
    if c == 1:
        maior = peso
        menor = peso
    else:
        # Atualiza maior
        if peso > maior:
            maior = peso
        # Atualiza menor
        if peso < menor:
            menor = peso

print(f'\nO maior peso lido foi {maior} kg.')
print(f'O menor peso lido foi {menor} kg.')

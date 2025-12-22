galeria = []
dados = []

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))

    galeria.append(dados[:])
    dados.clear()

    cont = input('Quer continuar? [S/N] ').strip().upper()[0]
    if cont == 'N':
        break
print('-='*30)
# ------------------------------------------------------

# A) Quantas pessoas foram cadastradas
print(f'\nTotal de pessoas cadastradas: {len(galeria)}')

# B e C) Achar maior e menor peso
# Pegando o peso da primeira pessoa como referência
maior_peso = menor_peso = galeria[0][1]

for pessoa in galeria:
    peso = pessoa[1]
    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso

# Agora listamos quem tem esses pesos
mais_pesadas = []
mais_leves = []

for pessoa in galeria:
    if pessoa[1] == maior_peso:
        mais_pesadas.append(pessoa[0])
    if pessoa[1] == menor_peso:
        mais_leves.append(pessoa[0])

# ------------------------------------------------------

# Resultados finais
print(f'\nMaior peso: {maior_peso} Kg. Pessoas: {mais_pesadas}')
print(f'Menor peso: {menor_peso} Kg. Pessoas: {mais_leves}')

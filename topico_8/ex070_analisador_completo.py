mulheres_menos_20 = 0
soma_idade = 0
mais_velho_idade = 0
mais_velho_nome = ''

print('-' * 40)
print('   ANÁLISE DE GRUPO - 4 PESSOAS')
print('-' * 40)

for cont in range(1, 5):
    print(f'\n--- {cont}ª PESSOA ---')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()[0]

    soma_idade += idade

    # Mulheres com menos de 20
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

    # Homem mais velho
    if sexo == 'M' and idade > mais_velho_idade:
        mais_velho_idade = idade
        mais_velho_nome = nome

# Média da idade
media_idade = soma_idade / 4

print('\n' + '-' * 40)
print('RESULTADOS')
print('-' * 40)

print(f'Média de idade do grupo: {media_idade:.1f} anos')
print(f'Mulheres com menos de 20 anos: {mulheres_menos_20}')

if mais_velho_nome:
    print(f'Homem mais velho: {mais_velho_nome} ({mais_velho_idade} anos)')
else:
    print('Nenhum homem foi cadastrado.')

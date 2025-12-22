cadastro_p = dict()
grupo_p = list()
soma = media = 0
while True:
    cadastro_p.clear()
    cadastro_p['nome'] = str(input('Nome: '))

    while True:
        cadastro_p['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if cadastro_p['sexo'] in 'MF':
            break
        else:
            print('ERRO! Por favor, digite apenas M ou F.')
    cadastro_p['idade'] = int(input('Idade: '))
    soma += cadastro_p['idade']
    grupo_p.append(cadastro_p[:])

    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if resp in 'SN':
            break
    print('ERRO! Por favor, digite apenas S ou N.')
    if resp == 'N':
        break
print('=-'*30)
print(f'A)Ao todo foram {len(grupo_p)} pessoas cadastradas.')

media = soma / len(grupo_p)
print(f'B) A média de idade é {media:5.2f} anos.')

print('C) As mulheres cadastradas foram ', end='')
for p in grupo_p:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}' , end='')
print()

print('D) A média das idades foram ', end='')
for p in grupo_p:
    if p['idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
print('Fim')
print('=-'*30)

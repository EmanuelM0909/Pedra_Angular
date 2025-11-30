import datetime

ano_atual = datetime.datetime.now().year
maiores = 0
menores = 0

for usuario in range(1, 8):
    ano = int(input(f'Ano de nascimento do usuário {usuario}: '))
    idade = ano_atual - ano

    if idade < 18:
        menores += 1
    else:
        maiores += 1

print(f'Maiores de idade: {maiores}')
print(f'Menores de idade: {menores}')

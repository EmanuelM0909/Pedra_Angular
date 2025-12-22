l = []

while True:
    num = int(input('Digite um número: '))
    l.append(num)

    continuar = input('Quer continuar? [S/N]: ').strip().upper()

    if continuar == 'N':
        print('Fim da leitura!')
        break
    elif continuar != 'S':
        print('Opção inválida! Encerrando por segurança...')
        break

# A) Quantos números foram digitados
print(f'\nVocê digitou {len(l)} números.')

# B) Lista em ordem decrescente
print(f'Lista em ordem decrescente: {sorted(l, reverse=True)}')

# C) Verificar se o número 5 aparece
if 5 in l:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 NÃO apareceu na lista.')

l = []
par = []
impar = []

while True:
    num = int(input("Digite um valor: "))
    l.append(num)

    # separando par/ímpar
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

    continuar = input("Quer continuar? [S/N] ").upper().strip()[0]
    if continuar == 'N':
        print('Fim da adição dos valores.')
        break
    if continuar != 'S':
        print('Opção inválida! Encerrando por segurança...')
        break

# a) lista completa
print(f'\nLista completa: {l}')
# b) lista só com pares
print(f'Lista de pares: {par}')
# c) lista só com ímpares
print(f'Lista de ímpares: {impar}')

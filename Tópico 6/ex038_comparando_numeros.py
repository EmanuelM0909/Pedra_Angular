n1 = int(input('Digite o primerio número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print(f'O número {n1} é maior que {n2}!')
    print('O PRIMEIRO número é maior!')
elif n2 > n1:
    print(f'O número {n2} é maior que {n1}!')
    print('O SEGUNGO número é maior!')
elif n1 == n2:
    print(f'O número {n1} e o número {n2} são iguais!')
else:
    print('Erro, Tente novamente!!!')

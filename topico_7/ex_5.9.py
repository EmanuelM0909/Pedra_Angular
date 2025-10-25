'''Exercício 9: Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo, assim como o resto da divisão. Utilize apenas
os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender o quociente da divisão de dois números como a quantidade
de vezes que podemos retirar o divisor do dividendo. Logo, 20 ÷ 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20.'''

dividendo = int(input('Digite um número para ser nosso dividendo: '))
divisor = int(input('Digite outro número diferente != de 0 para ser o divisor: '))

if divisor == 0:
    print('Erro: não é possível dividir por zero!')
else:
    cont = 0
    resto = dividendo

    while resto >= divisor:
        resto -= divisor
        cont += 1
print(f'\nResultado da divisão:')
print(f'{dividendo} ÷ {divisor} = {cont} com resto {resto}')

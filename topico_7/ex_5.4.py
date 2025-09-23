'''Exercício 4: Modifique o programa anterior para imprimir de 1 até o número digitado pelo usuário,
 mas, dessa vez, apenas os números ímpares.'''
fim = int(input('Digite um número para ser o final da contagem: '))
x = 0  # começamos em 0
while x <= fim:  # queremos até o valor digitado pelo usuário
    if x % 2 != 0:  # condição para ímpar
        print(x)  # imprimi o valor atual
    x = x + 1  # incrementa o contador

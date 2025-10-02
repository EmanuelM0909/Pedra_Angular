'''Exercício 4: Modifique o programa anterior para imprimir de 1 até o número digitado pelo usuário,
 mas, dessa vez, apenas os números ímpares.'''
fim = int(input('Digite um número para ser o final da contagem: '))
cont = 0  # começamos em 0
while cont <= fim:  # queremos até o valor digitado pelo usuário
    if cont % 2 != 0:  # condição para ímpar
        print(cont)  # imprimi o valor atual
    cont += 1  # incrementa o contador
print(f'Esses são os números ímpares até {fim}')

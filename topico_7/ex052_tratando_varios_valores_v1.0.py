n = contador = soma = 0
n = int(input('Digite um número [999 para o programa]: '))
while n != 999:
    soma += n
    contador += 1
    n = int(input('Digite um número [999 para o programa]: '))
print(f'Você digitou {contador} números. a soma deles é {soma}')
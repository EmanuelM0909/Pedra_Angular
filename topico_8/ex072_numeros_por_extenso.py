t = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Digite um número de 0 a 20: '))
if num < 0 or num > 20:
    print(f'{num} não se encontra entre 0 e 20. Digite um número de 0 a 20.')
else:
    print(f'Você escolheu {t[num]}')

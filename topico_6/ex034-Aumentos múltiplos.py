salario = float(input('Qual é o vlaor do seu salario: '))
media = 1250.00
if salario > media:
    novo = salario + (salario * 10 / 100)
    print(f'O aumento de salario foi de R${novo}.')
else:
    novo = salario + (salario * 15 / 100)
    print(f'O aumento foi de R${novo}.')

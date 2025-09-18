velocidade = float(input('Digite a velocidade do carro: '))

if velocidade > 80:
    print('Você ultrapassou o limite de velocidade.')
    multa = (velocidade - 80) * 7
    print(f'Sua multa é de R${multa:.2f}')
else:
    print('Tudo tranquilo, você está dentro do limite de velocidade.')

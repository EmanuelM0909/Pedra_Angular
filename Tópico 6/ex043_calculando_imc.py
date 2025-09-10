nome = str(input('Qual é o seu nome : '))
peso = float(input('Qual é o seu peso: '))
altura = float(input('Qual a sua altura: '))
imc = peso / (altura * altura)
print(f'{nome}, seu IMC é de {imc}')
if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc <= 25:
    print('Você está no peso ideal.')
elif 25 < imc <= 30:
    print('Você está sobrepeso.')
elif 30 < imc <= 40:
    print('Você está obeso.')
elif imc > 40:
    print('Você está com obesidade mórbida.')
else:
    print('Erro. Tente novamente.')

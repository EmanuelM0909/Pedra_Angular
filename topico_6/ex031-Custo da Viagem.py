distancia = float(input('Qual a distancia da viagem em KM: '))
p1 = distancia * 0.50
p2 = distancia * 0.45
if distancia <= 200:
    print(f'O valor da sua corrida foi de R${p1:.2f}')
else:
    print(f'O valor acima de 200km fica mais barato e valor fica de R${p2:.2f}')

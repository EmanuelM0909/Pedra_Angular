dias = int(input('Quantos dias alugados: '))
km = float(input('Quantos KM rodados: '))
p1 = dias * 60
p2= km * 0.15
total = p1 + p2
print(f'O total a pagar é de R%{total:.2f}')

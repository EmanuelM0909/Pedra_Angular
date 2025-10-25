num  = float(input("Digite um número para encontrar a sua raiz quadrada: "))
b = 2
p = (b + (num / b)) / 2
while abs(num - (p * p)) > 0.0001:
    b = p
    p = (b + (num / b)) / 2
print(f'A raiz quad. de {num} é aproximadamente {p}')


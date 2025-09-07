from math import sqrt
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento cateto adjacente: '))
hip = sqrt(co **2 + ca ** 2)
print(f'A hipotenusa vai medir {hip:.2f}')
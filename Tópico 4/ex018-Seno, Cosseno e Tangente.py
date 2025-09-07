import math
an = float(input('Digite um ângulo: '))
rad = math.radians(an)
print(f'O seno de {an} é {math.sin(rad):.2f}')
print(f'O cosseno de {an} é {math.cos(rad):.2f}')
print(f'A tangente de {an} é {math.tan(rad):.2f}')
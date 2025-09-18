"""# Lê os três números
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

# Descobre o maior e o menor
maior = max(n1, n2, n3)
menor = min(n1, n2, n3)

# Mostra o resultado
print(f'O maior número digitado foi {maior}')
print(f'O menor número digitado foi {menor}')"""

a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
c = float(input('Digite o terceiro número: '))
# Verificando o menor!
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando o maior!
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')

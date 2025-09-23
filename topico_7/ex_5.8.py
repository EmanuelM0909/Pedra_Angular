'''Exercício 8: Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e
subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles. Assim, 4 × 5 = 5
+ 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.'''

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

resultado = 0
x = 0

while x < b:        # soma 'a' exatamente 'b' vezes
    resultado = resultado + a
    x = x + 1

print(f"{a} x {b} = {resultado}")

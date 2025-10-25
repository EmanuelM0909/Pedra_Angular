'''Exercício 8: Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e
subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles. Assim, 4 × 5 = 5
+ 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.'''
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

resultado = 0      # aqui guardaremos o valor final da multiplicação
cont = 0           # contador para controlar quantas vezes já somamos

while cont < num2:   # repetiremos enquanto não atingirmos o número de vezes
    resultado += num1   # soma o primeiro número em "resultado"
    cont += 1           # aumenta o contador em 1 (controla as repetições)

print(f"O resultado de {num1} x {num2} é {resultado}")

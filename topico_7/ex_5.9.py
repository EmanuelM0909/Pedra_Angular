'''Exercício 9: Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo, assim como o resto da divisão. Utilize apenas
os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender o quociente da divisão de dois números como a quantidade
de vezes que podemos retirar o divisor do dividendo. Logo, 20 ÷ 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20.'''

a = int(input("Digite o dividendo: "))
b = int(input("Digite o divisor: "))

quociente = 0
resto = a

while resto >= b:     # enquanto ainda dá para subtrair
    resto = resto - b
    quociente = quociente + 1

print(f"{a} ÷ {b} = {quociente} (resto {resto})")

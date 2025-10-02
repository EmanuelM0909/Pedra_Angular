'''Exercício 6: Altere o programa anterior para exibir os resultados no mesmo formato de uma tabuada: 2x1 = 2, 2x2=4, ...'''
num = int(input('Tabuada de: '))
cont = 0
while cont <= 10:
    mult = cont * num
    print(mult)
    cont += 1
print(f'A cima temos a Tabuada de multiplicação de {num}')

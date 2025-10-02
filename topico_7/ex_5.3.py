'''Exercício 3: Faça um programa para escrever a contagem regressiva do lançamento de um foguete.
O programa deve imprimir 10, 9, 8, ..., 1, 0 e Fogo! na tela.'''
cont = 1  # acabamos em 1
while cont >= 10:  # queremos até os 10 primeiros
    print(cont)  # imprimi o valor atual
    cont -= 1  # diminui o contador

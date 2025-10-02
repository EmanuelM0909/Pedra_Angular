'''Exercício 7: Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada,
 em vez de começar com 1 e 10.'''

''' Primeira vez.
num = int(input('Tabuada de: '))
inicio = int(input('Digite de onde devemos começar: '))
fim = int(input('Digite onde vamos terminar: '))
cont = 0   # ❌ ERRO 1: contador começou em 0
while fim >= inicio:   # ❌ ERRO 2: condição nunca muda
    mult = inicio * cont   # ❌ ERRO 3: está multiplicando o "inicio" e não o "num"
    print(mult)
    cont += 1
print('fim')
'''

#resposta correta!!!

num = int(input('Tabuada de: '))
inicio = int(input('Digite de onde devemos começar: '))
fim = int(input('Digite onde vamos terminar: '))

cont = inicio  #  começa do valor escolhido pelo usuário

while cont <= fim:  #  repete até o contador chegar ao fim
    mult = num * cont  #  agora multiplica pelo número da tabuada
    print(f'{num} x {cont} = {mult}')  #  saída formatada
    cont += 1  #  incrementa o contador

print('fim')

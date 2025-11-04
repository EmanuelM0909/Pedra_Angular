expressao = input('Digite a sequência de parênteses a validar: ')
pilha = []
cont = 0
while cont < len(expressao):
    if expressao[cont] == '(':
        pilha.append('(')
    if expressao[cont] == ')':
        if len(pilha) > 0:
            topo = pilha.pop(-1)
        else:
            pilha.append(')')
            break
    cont += 1
if len(pilha) == 0:
    print('Ok')
else:
    print('Erro')
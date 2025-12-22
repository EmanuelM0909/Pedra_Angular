''' expressao = input("Digite uma expressão: ")

contador = 0
valida = True

for caractere in expressao:
    if caractere == '(':
        contador += 1
    elif caractere == ')':
        if contador > 0:
            contador -= 1
        else:
            valida = False
            break

if valida and contador == 0:
    print("Expressão correta!")
else:
    print("Expressão incorreta!") '''

expressao = str(input("Digite uma expressão: "))
pilha = []
for caractere in expressao:
    if caractere == '(':
        pilha.append('(')
    elif caractere == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print("Expressão correta!")
else:
    print("Expressão incorreta!")

primeira = []
segunda = []
while True:
    valor = int(input('Digite um valor para adicionar a primeira lista: [digite 0 para finalizar]'))
    if valor == 0:
        print('Fim da primeira lista.')
        break
    primeira.append(valor)
    #print(primeira)
while True:
    valor = int(input('Digite um valor para adicionar a segunda lista: [digite 0 para finalizar]'))
    if valor == 0:
        print('Fim da segunda lista.')
        break
    segunda.append(valor)
    #print(segunda)
terceira = primeira[:]
terceira.extend(segunda)
cont = 0
while cont < len(terceira):
    print(f'{cont}: {terceira[cont]}')
    cont += 1


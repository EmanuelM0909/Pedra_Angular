l = []
while True:
    num = (int(input('Digite um valor: ')))
    if num in l:
        print("Esse item já está na lista, tente outro número!")
    if num not in l:
        l.append(num)
        print('Adicionado com sucesso!!')
    while True:
        continuacao = input('Quer continuar: [S/N]').strip().upper()[0]
        if continuacao == 'N':
            print('Fim!!!')
            l.sort()
            print(f'Lista final: {l}')
            break
        elif continuacao == 'S':
            break
        else:
            print('Erro!!! Tente novamente.')


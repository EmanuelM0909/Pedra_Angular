valor = float(input('digite o valor a pagar: '))
ced = 0
atual = 100
a_pagar = valor
while True:
    if atual <= a_pagar:
        a_pagar -= atual
        a_pagar = round(a_pagar, 2)
        ced += 1
    else:
        if ced > 0:
            print(f'{ced} cédula(s)/moeda(s) de R${atual:.2f}')
        if a_pagar < 0.01:
            break
        if atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        elif atual == 1:
            atual = 0.50
        elif atual == 0.50:
            atual = 0.10
        elif atual == 0.10:
            atual = 0.05
        elif atual == 0.05:
            atual = 0.01
        ced = 0

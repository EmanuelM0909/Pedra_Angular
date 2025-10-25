print("Contagem de cédulas")

valor = int(input("Digite o valor a pagar: "))
cedulas = 0
atual = 100  # Começamos agora com a nota de R$100
a_pagar = valor

while True:
    if atual <= a_pagar:
        a_pagar -= atual
        cedulas += 1
    else:
        print(f"{cedulas} cédula(s) de R${atual}")
        if a_pagar == 0:
            break
        # Troca de cédula conforme a ordem decrescente
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
        cedulas = 0  # zera o contador de cédulas

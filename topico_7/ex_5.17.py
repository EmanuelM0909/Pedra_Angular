#  Programa: Teste sobre Contagem de Cédulas

print("=" * 50)
print(" Teste de Lógica — Contagem de Cédulas")
print("=" * 50)

# Mostra o código do exercício de forma visual
print("""
----------------------------------------------
print("Programa: Contagem de cédulas.")
print("Execute o programa com os valores: 501, 745, 384, 2, 7 e 1.")

valor = int(input("Digite o valor a pagar: "))
cedulas = 0
atual = 50
a_pagar = valor

while True:
    if atual <= a_pagar:
        a_pagar -= atual
        cedulas += 1
    else:
        print(f"{cedulas} cédula(s) de R${atual}")
        if a_pagar == 0:
            break
        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cedulas = 0
----------------------------------------------
""")

# Pergunta interativa ao usuário
print("\nAgora, responda à pergunta abaixo :")
while True:
    resposta = input("O que acontece quando se digita 0 (zero) no valor a pagar? ").strip().upper()

    if resposta == "PARA":
        print("\n Você acertou! O programa PARA por causa do 'break'.")
        break
    else:
        print(" Resposta errada. Tente novamente!\n")

from time import sleep

# Primeiro pedimos dois números para o usuário
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

opcao = 0  # variável de controle do menu

# Enquanto o usuário não escolher sair (5), o programa continua
while opcao != 5:
    print("\n\033[34m==== MENU PRINCIPAL ====\033[m")  # título azul
    print("\033[32m[ 1 ] Somar\033[m")
    print("\033[33m[ 2 ] Multiplicar\033[m")
    print("\033[35m[ 3 ] Maior\033[m")
    print("\033[36m[ 4 ] Novos números\033[m")
    print("\033[31m[ 5 ] Sair do programa\033[m")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:  # SOMAR
        soma = n1 + n2
        print(f"\033[32mA soma entre {n1} + {n2} = {soma}\033[m")
    elif opcao == 2:  # MULTIPLICAR
        mult = n1 * n2
        print(f"\033[33mA multiplicação entre {n1} x {n2} = {mult}\033[m")
    elif opcao == 3:  # MAIOR
        if n1 > n2:
            print(f"\033[35mO maior número é {n1}\033[m")
        elif n2 > n1:
            print(f"\033[35mO maior número é {n2}\033[m")
        else:
            print("\033[35mOs dois números são iguais!\033[m")
    elif opcao == 4:  # NOVOS NÚMEROS
        print("\033[36mDigite novos números:\033[m")
        n1 = int(input("Novo primeiro número: "))
        n2 = int(input("Novo segundo número: "))
    elif opcao == 5:  # SAIR
        print("\033[31mFinalizando o programa... Até logo!\033[m")
    else:  # OPÇÃO INVÁLIDA
        print("\033[7;31mOpção inválida! Tente novamente.\033[m")

    sleep(1)  # pausa de 1 segundo só para dar mais realismo

print("\033[34mPrograma encerrado com sucesso!\033[m")

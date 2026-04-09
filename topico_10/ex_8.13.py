def ler_opcao(opcoes_validas):

    opcoes_validas = opcoes_validas.lower()

    while True:
        opcao = input("Digite uma opção: ").lower()

        if opcao in opcoes_validas:
            return opcao
        else:
            print("Opção inválida, tente novamente.")


resultado = ler_opcao("SN")
print("Opção escolhida:", resultado)
palavra = input("Digite a palavra secreta: ").lower().strip()

# limpa a tela
for _ in range(100):
    print()

digitadas = []
acertos = []
erros = 0

while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(f"\nPalavra: {senha}")

    if senha == palavra:
        print(" Você acertou!")
        break

    tentativa = input("Digite uma letra: ").lower().strip()

    if tentativa in digitadas:
        print("️ Você já tentou essa letra!")
        continue
    else:
        digitadas.append(tentativa)
        if tentativa in palavra:
            acertos.append(tentativa)
        else:
            erros += 1
            print(" Você errou!")

    # desenho da forca
    print("\nX==:==")
    print("X  :   ")
    print("X  O   " if erros >= 1 else "X")

    linha2 = ""
    if erros == 2:
        linha2 = "  |   "
    elif erros == 3:
        linha2 = " \\|   "
    elif erros >= 4:
        linha2 = " \\|/ "
    print(f"X{linha2}")

    linha3 = ""
    if erros == 5:
        linha3 = " /    "
    elif erros >= 6:
        linha3 = " / \\ "
    print(f"X{linha3}")

    print("X")
    print("===========")

    if erros == 6:
        print(" Enforcado!")
        print(f"A palavra secreta era: {palavra}")
        break

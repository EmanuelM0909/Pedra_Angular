import random

# lista de palavras
palavras = ["casa", "bola", "uva", "cobra", "python", "computador", "teclado"]

# escolhe uma palavra aleatória
palavra = random.choice(palavras)

# limpa a tela
for _ in range(100):
    print()

digitadas = []
acertos = []
erros = 0

while True:
    senha = ""

    # monta a palavra escondida
    for letra in palavra:
        senha += letra if letra in acertos else "."

    print(f"\nPalavra: {senha}")

    # condição de vitória
    if senha == palavra:
        print(" Você acertou!")
        break

    tentativa = input("Digite uma letra: ").lower().strip()

    # verifica repetição
    if tentativa in digitadas:
        print(" Você já tentou essa letra!")
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

    # condição de derrota
    if erros == 6:
        print(" Enforcado!")
        print(f"A palavra secreta era: {palavra}")
        break
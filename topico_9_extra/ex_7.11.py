# ================================
# LISTA DE PALAVRAS
# ================================
palavras = [
    "casa",
    "bola",
    "mangueira",
    "uva",
    "quiabo",
    "computador",
    "cobra",
    "lentilha",
    "arroz",
]

# ================================
# CÁLCULO DO ÍNDICE DA PALAVRA
# ================================
numero = int(input("Digite um número: "))
indice = (numero * 776) % len(palavras)
palavra = palavras[indice]

# ================================
# LIMPA A TELA
# ================================
for _ in range(100):
    print()

# ================================
# VARIÁVEIS DO JOGO
# ================================
digitadas = []
acertos = []
erros = 0

# ================================
# DESENHO BASE DA FORCA
# (lista de listas)
# ================================
desenho = [
    list("X==:=="),
    list("X  :  "),
    list("X     "),
    list("X     "),
    list("X     "),
    list("X     "),
    list("======="),
]

# ================================
# JOGO
# ================================
while True:
    # Monta a palavra escondida
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(f"\nPalavra: {senha}")

    # Vitória
    if senha == palavra:
        print(" Você acertou!")
        break

    tentativa = input("Digite uma letra: ").lower().strip()

    # Letra repetida
    if tentativa in digitadas:
        print(" Você já tentou essa letra!")
        continue

    digitadas.append(tentativa)

    # Acerto ou erro
    if tentativa in palavra:
        acertos.append(tentativa)
    else:
        erros += 1
        print(" Você errou!")

        # DESENHA O BONECO (por erro)
        if erros == 1:
            desenho[2][3] = "O"      # cabeça
        elif erros == 2:
            desenho[3][3] = "|"      # tronco
        elif erros == 3:
            desenho[3][2] = "\\"     # braço esquerdo
        elif erros == 4:
            desenho[3][4] = "/"      # braço direito
        elif erros == 5:
            desenho[4][2] = "/"      # perna esquerda
        elif erros == 6:
            desenho[4][4] = "\\"     # perna direita

    # IMPRIME A FORCA
    print()
    for linha in desenho:
        print("".join(linha))

    # Derrota
    if erros == 6:
        print("\n Enforcado!")
        print(f"A palavra secreta era: {palavra}")
        break

tabuleiro = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]

jogador_atual = "X"
contador_jogadas = 0

ganho = [
    [0, 1, 2],  # linhas
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],  # colunas
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],  # diagonais
    [2, 4, 6]
]

while True:
    print(f"""
 {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}
---+---+---
 {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}
---+---+---
 {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}
""")

    jogada = int(input(f"Escolha uma posição (1 a 9) jogador {jogador_atual}: "))
    posicao = jogada - 1

    #  Verificar se a posição é válida
    if posicao < 0 or posicao > 8:
        print("Posição inválida!")
        continue

    #  Verificar se a casa está vazia
    if tabuleiro[posicao] != " ":
        print("Essa posição já está ocupada!")
        continue

    #  Marcar jogada
    tabuleiro[posicao] = jogador_atual
    contador_jogadas += 1

    #  Verificar vitória (apenas após 5 jogadas)
    if contador_jogadas >= 5:
        for combinacao in ganho:
            if (tabuleiro[combinacao[0]] ==
                tabuleiro[combinacao[1]] ==
                tabuleiro[combinacao[2]] == jogador_atual):
                print(f"Jogador {jogador_atual} venceu!")
                break
        else:
            # ninguém ganhou ainda
            pass
        if contador_jogadas >= 5:
            if any(
                tabuleiro[c[0]] ==
                tabuleiro[c[1]] ==
                tabuleiro[c[2]] == jogador_atual
                for c in ganho
            ):
                break

    # Verificar empate
    if contador_jogadas == 9:
        print("Deu velha!")
        break

    # Trocar jogador
    jogador_atual = "O" if jogador_atual == "X" else "X"

import random
import time

# --- Cabeçalho ---
print("\033[31m=== Caçada a Jupter!!! ===\033[m")

# --- Escolha de dificuldade ---
nivel = input("\033[93mEscolha o nível (facil / medio / dificil): \033[m").lower()

if nivel == "facil":
    vida_personagem = 100
    dano = 20
elif nivel == "medio":
    vida_personagem = 80
    dano = 25
elif nivel == "dificil":
    vida_personagem = 75
    dano = 30
else:
    print("Nível inválido! Definindo como fácil.")
    vida_personagem = 100
    dano = 20

tentativas = 5

# --- Explicação ---
print("\033[92mObjetivo: achar o Alienígena antes dele te derrotar!")
print("Você tem 5 tentativas.\033[m")

# --- Número secreto ---
arvore = random.randint(1, 100)

print("\033[94mO alienígena se escondeu em uma das 100 árvores...")
print("Cada erro custa vida!\033[m")

# --- Loop principal ---
while tentativas > 0 and vida_personagem > 0:
    print(f"\n❤️ Vida: {vida_personagem}% | 🎯 Tentativas: {tentativas}")

    try:
        palpite = int(input("\033[1;32mDigite um palpite:\033[m "))
    except:
        print("❌ Digite apenas números!")
        continue

    if palpite == arvore:
        print("\033[92m🎯 Parabéns!!! Você encontrou o alienígena!!!\033[m")
        break
    else:
        # --- Efeito de ataque ---
        print("\033[91m👽 Alienígena atirando...\033[m")
        time.sleep(0.5)
        print("\033[91m💥 ACERTOU!\033[m")

        vida_personagem -= dano
        tentativas -= 1

        # --- Dica ---
        if palpite < arvore:
            print("🔼 O alienígena está em uma árvore MAIOR!")
        else:
            print("🔽 O alienígena está em uma árvore MENOR!")

        print(f"Você perdeu {dano}% de vida!")

        # --- Estado do jogador ---
        if vida_personagem > 60:
            print("🟢 Você ainda está bem!")
        elif vida_personagem > 30:
            print("🟡 Você está ferido!")
        else:
            print("🔴 Você está quase morrendo!")

# --- Fim de jogo ---
if vida_personagem <= 0:
    print(f"\n\033[91m💀 Você morreu! O alienígena estava na árvore {arvore}.\033[m")

elif tentativas == 0:
    print(f"\n\033[91m💀 Você ficou sem tentativas! O alienígena estava na árvore {arvore}.\033[m")
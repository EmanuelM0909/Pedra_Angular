import random

vida_personagem = 100
tentativas = 5

print("\033[31mCaçada a Jupter!!!\033[m")

print("\033[92mObjetivo: achar o Alienígena antes dele te derrotar!"
      "\nVocê tem 5 tentativas.\033[m")

arvore = random.randint(1, 100)

print("\033[94mO alienígena se escondeu em uma das 100 árvores..."
      "\nCada erro custa 20% de vida!\033[m")

while tentativas != 0:
    print(f"\nVida: {vida_personagem}% | Tentativas: {tentativas}")

    try:
        palpite = int(input("Digite um palpite: "))
    except:
        print("Digite apenas números!")
        continue

    if palpite == arvore:
        print(" Parabéns!!! Você encontrou o alienígena!!!")
        break
    else:
        vida_personagem -= 20
        tentativas -= 1

        if palpite < arvore:
            print(" Está em uma árvore MAIOR!")
        else:
            print(" Está em uma árvore MENOR!")

        print(f"Você perdeu 20% de vida. Agora tem {vida_personagem}%.")

if tentativas == 0:
    print(f"\n Você perdeu! O alienígena estava na árvore {arvore}.")
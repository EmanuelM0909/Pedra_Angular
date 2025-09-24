from random import randint
pc = randint(0, 10)
print(" BEM-VINDO(A) AO NOSSO JOGO DE ADIVINHA!!!"
      "\n O pc irá pensar em um número de 0 à 10."
      "\n Vamos começar...")
acerto = False
palpites = 0
while not acerto:
    jogador = int(input("Escolha um número de 0 a 10 e veja se você acertou os pensamentos do PC: "))
    palpites += 1
    if jogador == pc:
        acerto = True
    else:
        if jogador < pc:
            print('Mais... Tente outra vez!!!')
        elif jogador > pc:
            print('Menos... Tente outra vez!!!')
print(f'Você acertou com {palpites} tentativas.')

import random
from time import sleep

print("Escolha uma opção:")
print("[0] Pedra")
print("[1] Papel")
print("[2] Tesoura")

opcoes = ["Pedra", "Papel", "Tesoura"]
computador = random.randint(0, 2)
jogador = int(input("Digite o número da sua jogada: "))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('-=' * 10)
print(f"Você jogou {opcoes[jogador]}")
print(f"O computador jogou {opcoes[computador]}")
print('-=' *10)

if jogador == computador:
    print("Empate!")
elif (jogador == 0 and computador == 2) or \
     (jogador == 1 and computador == 0) or \
     (jogador == 2 and computador == 1):
    print("Você venceu!")
else:
    print("Você perdeu!")

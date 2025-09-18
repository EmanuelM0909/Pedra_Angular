from random import randint
from time import sleep

# Computador pensa em um número
pc = randint(0, 5)

print("BEM-VINDO(A) AO NOSSO JOGO DE ADIVINHA!!!")
print("Vamos começar...")

# Jogador escolhe um número
jogador = int(input("Escolha um número de 0 a 5 e veja se você acertou os pensamentos do PC: "))

print("Processando...")
sleep(2)  # espera 2 segundos para dar suspense

# Verifica se acertou
if jogador == pc:
    print(" Parabéns, Você acertou!")
else:
    print(f" Infelizmente não foi dessa vez. O número que eu pensei foi {pc}.")

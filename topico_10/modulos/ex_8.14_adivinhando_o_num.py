import random
n = random.randint(1, 10)
tentativa = 0
while tentativa < 3:
    x = int(input("Escolha um numero entre 1 e 10: "))
    if x == n:
        print("Correto")
        break
    else:
        print("Erro")
    tentativa += 1
from random import randint

def linha():
    print("-" * 30)

def maior(*numeros):
    print("-" * 30)
    print("Analisando os valores:", numeros)

    maior_valor = numeros[0]

    for n in numeros:
        if n > maior_valor:
            maior_valor = n

    print(f"O maior valor é {maior_valor}")

# sorteando 3 números
maior(randint(1, 100), randint(1, 100), randint(1, 100))
linha()

# sorteando 5 números
maior(
    randint(1, 100),
    randint(1, 100),
    randint(1, 100),
    randint(1, 100),
    randint(1, 100)
)
linha()

# sorteando 8 números
maior(
    randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100),
    randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100)
)
linha()

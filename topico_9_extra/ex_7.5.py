base = input("Digite a primeira string: ")
origem = input("Digite a segunda string: ")
destino = input("Digite a terceira string: ")

resultado = ""

for letra in base:
    if letra in origem:
        posicao = origem.index(letra)
        resultado += destino[posicao]
    else:
        resultado += letra

print("Resultado:", resultado)

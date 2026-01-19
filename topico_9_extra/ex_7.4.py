sequencia = str(input("Digite uma string: ")).split()

contador = {}

for letra in sequencia:
    if letra in contador:
        contador[letra] += 1
    else:
        contador[letra] = 1
for chave in contador:
    print(chave, contador[chave])
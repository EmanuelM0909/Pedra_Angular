frase = input("Digite uma frase: ").lower()

troca = {
    'á':'a', 'à':'a', 'â':'a', 'ã':'a',
    'é':'e', 'ê':'e',
    'í':'i',
    'ó':'o', 'ô':'o', 'õ':'o',
    'ú':'u'
}

vogais = "aeiou"
contador = {}

for letra in frase:
    if letra in troca:
        letra = troca[letra]

    if letra in vogais:
        if letra in contador:
            contador[letra] += 1
        else:
            contador[letra] = 1

if contador:
    print("Contagem de vogais:")
    for v in contador:
        print(v, "=", contador[v])
else:
    print("Nenhuma vogal encontrada.")

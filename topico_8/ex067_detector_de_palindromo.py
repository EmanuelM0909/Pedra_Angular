frase = str(input('Digite uma frase para verificarmos se é um Palíndromo: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
invertido = ''
for letra in range(len(junto) -1, -1, -1):
    invertido += junto[letra]
if invertido == junto:
    print('É Palíndromo.')
else:
    print('Não é Palíndromo.')
print(f'Você digitou a frase {frase}')

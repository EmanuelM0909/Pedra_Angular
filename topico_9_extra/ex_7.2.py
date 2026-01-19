texto_1 = str(input("Digite uma frase: "))
texto_2 = str(input("Digite a segunda frase: "))
texto_3 = ''
for letra in texto_1:
    if letra in texto_2 and letra not in texto_3:
        texto_3 += letra
if texto_3 == '':
    print("Nenhum character em comum")
else:
    print(f"Character em comum: '{texto_3}'")


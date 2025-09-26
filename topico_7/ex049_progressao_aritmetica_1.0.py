a1 = int(input("Digite o primeiro termo (a1): "))
r = int(input("Digite a razão (r): "))

contador = 1
termo = a1

while contador <= 10:
    print(f"Termo {contador} = {termo}")
    termo += r
    contador += 1

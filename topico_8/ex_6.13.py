t = [-10, -8, 0, 1 ,2, 5, -2, -4]
maior = t[0]
menor = t[0]
soma = 0

for cont in t:
    soma += cont
    if cont > maior:
        maior = cont
    elif cont < menor:
        menor = cont

media = soma / len(t)

print(f"A maior temperatura foi {maior} e a menor foi {menor}.")
print(f"A média das temperaturas é {media:.2f}.")

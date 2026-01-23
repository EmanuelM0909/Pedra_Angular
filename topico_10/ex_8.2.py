print("Comparação de múltiplos!")
num_1 = int(input("Digite um número: "))
num_2 = int(input("Digite outro número: "))
print(f"Agora vamos ver se o {num_1} é multiplo de {num_2}: ")
def multiplo(a, b):
    if num_1 % num_2 == 0:
        return True
    else:
        return False
print(multiplo(num_1, num_2))
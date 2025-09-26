n = int(input("Digite um número inteiro não-negativo: "))

fatorial = 1
contador = 1

print(f"Calculando {n}! passo a passo:")

while contador <= n:
    print(f"{fatorial} x {contador} = {fatorial * contador}")
    fatorial *= contador
    contador += 1

print(f"\nO fatorial de {n} é {fatorial}")

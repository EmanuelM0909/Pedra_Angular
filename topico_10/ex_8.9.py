def fatorial(n):
    print(f"Calculando o fatorial de {n}")

    if n == 0 or n == 1:
        print(f"Fatorial de {n} é 1")
        return 1
    else:
        resultado = n * fatorial(n - 1)
        print(f"Fatorial de {n} é {resultado}")
        return resultado


# Programa principal
num = int(input("Digite um número: "))
print(f"Resultado final: {fatorial(num)}")

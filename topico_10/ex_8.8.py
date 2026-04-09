def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)


# Programa principal
x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))

resultado = mdc(x, y)
print(f"O MDC de {x} e {y} é {resultado}")

print("Área de um triângulo")
base = float(input("Digite o valor do primeiro base: "))
altura = float(input("Digite o valor do segundo altura: "))
def triangulo():
    area = base * altura / 2
    return area
print(f"A área obtida pela base {base} x a altura {altura} = {triangulo()}")

def linha():
    print("-="*30)

linha()
print("Calculando area")
linha()

def area():
    resultado = num1 * num2
    print(f"A area de um terreno {num2}X{num1} é de: {resultado}m²")


num1 = float(input("Digite o comprimento: "))
num2 = float(input("Digite a largura: "))
area()
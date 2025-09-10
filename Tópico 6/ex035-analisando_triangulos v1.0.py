print("verificar se três segmentos formam um triângulo")
a = float(input('Digite o um numero para o lado "a": '))
b = float(input('Digite o um numero para o lado "b": '))
c = float(input('Digite o um numero para o lado "c": '))
if a <= 0 and b <= 0 or c <= 0:
    print("O valores tem que ser superiores a 0")
if a < b + c and b < a + c and c < a + b:
    print("Pode formar um triângulo")
else:
    print("Não pode formar um triângulo")

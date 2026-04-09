import moeda
p = float(input("Digite o preço do produto: "))
print(f"O aumento foi de 50% e o novo preço é: {moeda.aumentar(p, 50)}")
print(f"A metade do aumento foi: {moeda.metade(p)}")
print(f"O dobro do aumento foi: {moeda.dobro(p)}")

lista_a = [1, 3, 2, 5, 4, 6, 7, 10]
lista_b = [1, 2, 3, 4, 5, 8, 9]
lista_c = []
cont = 0
while cont < len(lista_a):
    if lista_a not in lista_c:
        lista_c.append(lista_a[cont])
        cont += 1
cont = 0
while cont < len(lista_b):
    if lista_b not in lista_c:
        lista_c.append(lista_b[cont])
        cont += 1
print("Lista resultante (sem repetição):", lista_c)

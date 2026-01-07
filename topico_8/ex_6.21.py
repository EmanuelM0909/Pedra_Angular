#============Duas listas===========
a = [1, 3, 5, 7, 9, 2, 6]
b = [2, 4, 6, 8, 1, 3, 5]
#==Transformamos em conjuntos:=====
a = set(a)
b = set(b)

print(a, b)

print("\nRESUMO FINAL")
print("-" * 30)
print("Comuns:", a & b)
print("Só A:", a - b)
print("Só B:", b - a)
print("Não repetidos:", a ^ b)
print("A sem repetidos de B:", a - b)

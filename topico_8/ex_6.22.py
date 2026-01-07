#=====Lista antiga=====
a = [0, 9, 6, 4, 3, 4]
print(a)
#=====Lista atualizada=====
b = [0, 9, 5, 4, 4]
print(b)
#==Transformamos em conjuntos:=====
a = set(a)
b = set(b)

print("\nRESUMO FINAL")
print("-" * 30)
print("Comuns:", a & b)
print("Só A:", a - b)
print("Só B:", b - a)

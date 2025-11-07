l = []
while True:
    n = int(input("Digite um número (0 sai):"))
    if n == 0:
        break
    l.append(n)
for cont in l:
    print(cont)
print(l)

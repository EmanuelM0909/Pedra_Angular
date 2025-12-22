lista = []

for c in range(5):
    num = int(input(f"Digite o {c+1}º valor: "))

    # 1) Se a lista estiver vazia, adiciona direto
    if len(lista) == 0:
        lista.append(num)
        print("Adicionado no final da lista (primeiro elemento).")

    # 2) Se o número for MAIOR que o último elemento da lista, vai para o final
    elif num > lista[-1]:
        lista.append(num)
        print("Adicionado no final da lista.")

    # 3) Caso contrário, acha a posição certa para inserir
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f"Adicionado na posição {pos}.")
                break
            pos += 1

print("\nLista final ordenada:", lista)

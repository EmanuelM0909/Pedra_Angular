def verificar(texto, lista):
    for elemento in lista:
        if texto == elemento:
            return True

    return False


str = 'mel'
lista = ['maçã', 'ovo', 'pão', 'mel']

resultado = verificar(str, lista)
print(resultado)
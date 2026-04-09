def validacao_str(variavel, minimo, maximo):
    tamanho = len(variavel)

    if minimo <= tamanho <= maximo:
        return True
    else:
        return False


#programa principal
texto = input("Digite algo: ")

resultado = validacao_str(texto, 3, 10)

print(resultado)
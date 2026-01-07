texto = str(input("Digite uma frase: "))
busca = str(input("Digite a palavra que deseja buscar: "))
print(texto)
if busca in texto:
    print(f"'{busca}' foi encontrado na posição inicial {texto.find(busca)} do texto")
else:
    print('Erro, palavra não encontrada')
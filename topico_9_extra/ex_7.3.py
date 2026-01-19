primeira = str(input("Digite a primeira string: "))
segunda = str(input("Digite a segunda string: "))
terceira = ""
for letra in primeira:
    if letra not in segunda and letra not in terceira:
        terceira += letra
for letra in segunda:
    if letra not in primeira and letra not in terceira:
        terceira += letra

if terceira == "":
    print("Caracteres incomuns não encontrados")
else:
    print(f"Caracteres incomuns encontrados {terceira}")

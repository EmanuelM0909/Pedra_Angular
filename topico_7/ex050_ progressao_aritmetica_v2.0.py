a1 = int(input("Digite o primeiro termo (a1): "))
r = int(input("Digite a razão (r): "))
contador = 1
termo = a1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print(f"Termo {contador} = {termo}")
        termo += r
        contador += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer adicionar: '))
print(f'Progressão finalizada com sucesso!! Total de termos mostrados foi {total}')

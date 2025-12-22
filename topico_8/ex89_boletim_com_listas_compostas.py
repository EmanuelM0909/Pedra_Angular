# ---------------- SISTEMA DE BOLETIM — MODO FOX ---------------- #

lista = []      # Lista principal que guarda todos os alunos
temp = []       # Lista temporária para cada aluno individualmente

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))

    temp.append(nome)
    temp.append(nota1)
    temp.append(nota2)

    lista.append(temp[:])   # Copiando para a lista principal
    temp.clear()            # Limpando temporário

    continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break

# ---------------- BOLETIM GERAL ---------------- #

print('-=' * 30)
print(f'{"No.":<4}{"Nome":<20}{"Média":>8}')
print('-' * 34)
for i, aluno in enumerate(lista):
    nome = aluno[0]
    media = (aluno[1] + aluno[2]) / 2
    print(f'{i:<4}{nome:<20}{media:8.1f}')
print('-=' * 30)

# ---------------- CONSULTA INDIVIDUAL ---------------- #

while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('Finalizando...')
        break
    if 0 <= opc < len(lista):
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]:.1f} e {lista[opc][2]:.1f}')
    else:
        print('Número inválido! Tente novamente.')

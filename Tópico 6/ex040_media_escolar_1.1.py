print('ESCOLA BOM FIM')
materia = input('Qual materia sera as notas:')
print(f"{materia:=^20}")
print('Vamos para as notas:')
n1 = float(input('Digite a primeira nota do aluno:'))
n2 = float(input('Digite a segunda nota do aluno:'))
media = (n1 + n1) / 2
print(f'Tirando {n1} e {n2} a sua média é {media}')
'''– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO'''
if media >= 7.0:
    print('Parabéns, APROVADO!!!')
elif 7 > media >= 5:
    print('Foi quase, RECUPERAÇÃO!!!')
elif media < 5:
    print('Infelizmente não deu, REPROVADO!!!')
else:
    print('Erro, tente novamente.')
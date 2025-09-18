import random
aluno1 = input('Qual o nome do primerio aluno: ')
aluno2 = input('Qual o nome do segundo aluno: ')
aluno3 = input('Qual o nome do terceiro aluno: ')
aluno4 = input('Qual o nome do quarto aluno: ')
alunos = random.choice([aluno1, aluno2, aluno3, aluno4])
print(f'O escolhid foi {alunos}')
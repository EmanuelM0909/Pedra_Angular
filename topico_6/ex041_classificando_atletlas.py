#importação para verificar a idade!
from datetime import date
#Entrada de dados!
ano = int(input('Qual o ano de nascimento do atleta: '))
ano_atual = date.today().year
idade = ano_atual - ano
#Classificando categorias
if idade <= 9:
    print("Mirim")
elif idade <= 14:
    print("INFANTIL")
elif idade <= 19:
    print("JÚNIOR")
elif idade <= 25:
    print('SÊNIOR')
elif idade >= 26:
    print('MASTER')
else:
    print("Erro, tente novamente.")
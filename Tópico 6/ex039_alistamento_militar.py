from datetime import date
nome = str(input('Qual o seu nome: ')).strip()
ano = int(input('Qual o ano em que você nasceu: '))
ano_atual = date.today().year
idade = ano_atual - ano
print(f'{nome} você tem {idade} anos.')
if idade < 18:
    diferenca = idade - 18
    print(f'Para quem nasceu em {ano}, tem {idade} anos em {ano_atual}')
    print(f'Você ainda não consegue se alistar e falta {diferenca} anos')
    falta = ano_atual + diferenca
    print(f'Seu alistamento será em {falta} anos')
elif idade == 18:
    print('Esta na idade certa para se alistar. Procure a junta militar mais proxima.')
else:
    diferenca = 18 - idade
    multa = 5.82
    print(f'Já passou {diferenca} anos da hora de se alistar. \nProcure a Junta Militar e pague a multa de R${multa}')

'''from datetime import date

# Passo 1: pedir o ano de nascimento
ano_nascimento = int(input("Digite o ano em que você nasceu: "))

# Passo 2: pegar o ano atual
ano_atual = date.today().year

# Passo 3: calcular a idade
idade = ano_atual - ano_nascimento

print(f"Você tem {idade} anos.")

# Passo 4: verificar as condições
if idade == 18:
    print("Você deve se alistar IMEDIATAMENTE!")
elif idade < 18:
    faltam = 18 - idade
    print(f"Ainda faltam {faltam} ano(s) para o alistamento.")
    print(f"Seu alistamento será em {ano_atual + faltam}.")
else:
    atraso = idade - 18
    print(f"Você já deveria ter se alistado há {atraso} ano(s).")
    print(f"Seu alistamento foi em {ano_atual - atraso}.")
'''
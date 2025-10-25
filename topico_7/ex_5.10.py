'''Exercício 10: Modifique o programa para que aceite respostas com letras maiúsculas e minúsculas em todas as questões.

pontos = 0
questo = 1
while questão <= 3:
    resposta = input(f"Resposta da questão {questao}: ")
    if questão == 1 and resposta == "b":
        pontos = pontos + 1
    if questão == 2 and resposta == "a":
        pontos = pontos + 1
    if questão == 3 and resposta == "d":
        pontos = pontos + 1
    questão +=1
print(f"O aluno fez {pontos} ponto(s)")'''

#resposta:
pontos = 0
questao = 1

while questao <= 3:
    resposta = input(f"Digite a resposta da questão {questao}: ").upper().strip()

    if questao == 1 and resposta == "B":
        pontos += 1
    elif questao == 2 and resposta == "A":
        pontos += 1
    elif questao == 3 and resposta == "D":
        pontos += 1

    questao += 1

print(f"O aluno fez {pontos} ponto(s)")

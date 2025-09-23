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
    resposta = input(f"Resposta da questão {questao}: ")
    resposta = resposta.lower()  # transforma sempre em minúscula

    if questao == 1 and resposta == "b":
        pontos = pontos + 1
    if questao == 2 and resposta == "a":
        pontos = pontos + 1
    if questao == 3 and resposta == "d":
        pontos = pontos + 1

    questao += 1

print(f"O aluno fez {pontos} ponto(s)")

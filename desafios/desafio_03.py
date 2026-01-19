"""DESAFIO 3 — Dicionários (nível intermediário)
🎯 Objetivo:
Criar um programa que gerencie pessoas usando dicionários, com entrada de dados e análise no final.
📌 Requisitos
Crie um programa que:
Pergunte nome, idade e sexo de várias pessoas
Armazene cada pessoa em um dicionário com as chaves:
nome, idade, sexo
Guarde todos os dicionários dentro de uma lista
O programa deve parar quando o nome for vazio ("")
No final, mostre:
Quantas pessoas foram cadastradas
A lista completa
A média de idade
Todas as pessoas com idade acima da média
Todas as pessoas do sexo feminino
Exemplo de estrutura esperada (importante)
[
  {'nome': 'Ana', 'idade': 25, 'sexo': 'F'},
  {'nome': 'Carlos', 'idade': 40, 'sexo': 'M'}
]

 Dicas de lógica (sem entregar a resposta)
Crie um dicionário novo a cada volta do while
Use append() para colocar o dicionário na lista
Para a média:
soma das idades / quantidade
Para filtrar:
use for
use if pessoa['idade'] > media
use if pessoa['sexo'] == 'F'
 Regras
Não usar funções
Não usar bibliotecas
Tudo em um único arquivo
Apenas conteúdo que você já aprendeu"""

banco_dados = []
cont_sexo = 0
cont_idade = 0
soma_idade = 0

while True:
    nome = input("Digite o nome: ")

    if nome == "":
        break

    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M/F): ").upper()

    pessoa = {"nome": nome, "idade": idade, "sexo": sexo}
    banco_dados.append(pessoa)

    soma_idade += idade

if len(banco_dados) > 0:
    media = soma_idade / len(banco_dados)

    for pessoa in banco_dados:
        if pessoa["sexo"] == "F":
            cont_sexo += 1
            
    print(f"Ao total temos {len(banco_dados)} pessoas cadastradas.")
    print(f"Nosso banco de dados: {banco_dados}")
    print(f"Média de idade: {media}")
    print(f"Total de pessoas do sexo F: {cont_sexo}")
else:
    print("Nenhuma pessoa cadastrada.")

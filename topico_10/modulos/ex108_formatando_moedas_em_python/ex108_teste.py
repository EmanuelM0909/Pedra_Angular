from ex108_formatando_moedas_em_python import moeda
p = float(input("Digite o preço do produto: "))
print(f"Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}")
print(f"O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}")
print(f"A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}")
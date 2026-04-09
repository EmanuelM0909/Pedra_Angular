def ficha(jog = '<desconheicido>', gol = 0):
    print(f"O jogador {jog} fez {gol} gol(s) no campeonato.")

n = str(input("Diga o nome do jogador: "))
g = str(input("Quantidade de gols: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol = g)
else:
    ficha(n, g)
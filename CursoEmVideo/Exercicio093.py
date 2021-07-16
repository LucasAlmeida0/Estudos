aproveitamento = dict()
aproveitamento['nome'] = str(input('Nome: '))
partidas = int(input('Partidas: '))
gols = list()
for c in range(1, partidas+ 1):
    gols.append(int(input(f'Quantos gols foram feitos na {c}ª partida ')))

aproveitamento['gols'] = gols.copy()
aproveitamento['total'] = sum(gols)

print('-'*30)
print(aproveitamento)
print('-'*30)

for k, v in enumerate(aproveitamento):
    print(f'O campo {v} tem o valor {aproveitamento[v]}')

print('-'*30)

print(f"O jogador {aproveitamento['nome']} jogou {partidas} partidas.")
for x in range(0,partidas):
    print(f'=> Na partida {x+1}, fez {aproveitamento["gols"][x]} ')
print(f'Foi um total de {aproveitamento["total"]} gols')
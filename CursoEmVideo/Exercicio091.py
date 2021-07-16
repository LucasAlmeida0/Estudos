from random import randint
from operator import itemgetter
numeros = {}
ranking = list()
print('Valores sorteados: ')
for c in range(0,4):
    numeros[f'jogador{c+1}'] = randint(1,6)
    print(f'O jogador{c+1} tirou {numeros[f"jogador{c+1}"]} no dado')
print('=-'*20)
print('== RANKING DOS JOGADORES ==')
ranking = sorted(numeros.items(), key = itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}')




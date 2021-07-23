def ficha(nome='<desconhecido>',gols='0'):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato!'

jogador = str(input('Nome do Jogador: '))
numero = str(input('Número de Gols: '))

if numero.isnumeric():
    numero = int(numero)
else:
    numero = 0

if jogador.strip() == '':
    print(ficha(gols=numero))
else:
    print(ficha(jogador,numero))


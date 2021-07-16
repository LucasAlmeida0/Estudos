'''73 Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. 
Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

times = ('Athletico-PR', 'Fortaleza', 'Bragantino', 'Palmeiras', 'Atlético-MG','Fluminense','Bahia','Atlético-GO','Santos','Flamengo','Corinthians','Ceará SC','Internacional','Juventude','Sport Recife','Cuiabá','Chapecoense','São Paulo','América-MG','Grêmio')
cotador = 0
chapecoense = times.index('Chapecoense')
print('--' * 10)
print(f'Lista de times do Brasileirão: {times}')
print('--' * 10)
print(f'Os 5 são: {times[0:5]}')
print('--' * 10)
print(f'Os 4 últimos são: {times[-4:len(times)]}')
print('--' * 10)
print(f'Times em ordem alfabética: {sorted(times)}')
print('--' * 10)
print(f'O chapecoense está na {chapecoense + 1} posição')
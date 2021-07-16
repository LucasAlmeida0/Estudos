from random import randint
from time import sleep
numeros = []
dados = list()
print('-'*20)
print('MEGA SENA')
print('-'*20)
desejado = int(input('Quantos jogos você deseja que eu sorteie? '))
print(f'-=-= SORTEANDO {desejado} JOGOS -=-=')
for jogos in range(0 , desejado):

    for sorteador in range(0,6):
        while True:
            valor = randint(1,60)
            if sorteador == 0:
                dados.append(valor)
                break
            elif valor in dados:
                sorteador = sorteador - 1
            else:
                dados.append(valor)
                break
           
    numeros.append(dados[:])
    dados.clear()
    print(f'Jogo {jogos+1}: {numeros[jogos]}')
print('-=-=-= BOA SORTE  -=-=-=')


        

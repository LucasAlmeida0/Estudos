'''68 Faça um programa que jogue par ou ímpar com o computador.  O jogo só será interrompido quando o jogador perder, 
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
from random import randint
print('-'*20)
print('VAMOS JOGAR PAR OU IMPAR')
print('-'*20)
vitoria = 0
while True:
    print('-'*20)
    valor = int(input('Digite um valor: '))
    escolha = str(input('Par ou Impar: [P/I] ')).upper().strip()[0]
    print('-'*20)
    computador = randint(0, 10)
    total = computador + valor
    if escolha in 'P' and total % 2 == 0: 
        vitoria +=1 
        print(f'Você jogou {valor} e o computador jogou {computador}. Total de {total} deu PAR')
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
    elif escolha in 'I' and total % 2 != 0:
        vitoria +=1
        print(f'Você jogou {valor} e o computador jogou {computador}. Total de {total} deu IMPAR')
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
    elif total % 2 == 0:
        print(f'Você jogou {valor} e o computador jogou {computador}. Total de {total} deu PAR')
        print('Você PERDEU!')
        break
    else:
        print(f'Você jogou {valor} e o computador jogou {computador}. Total de {total} deu IMPAR')
        print('Você PERDEU!')
        break
print(f'GAME OVER! Você venceu {vitoria} vezes.')

        



#45 Crie um programa que faça o computador jogar Jokenpô com você.
import time
import random
print("Vamos jogar JO KEN PÔ?")
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA ''')
escolha = int(input("Qual é sua jogada? "))
print('--------------')
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO')
print('--------------')

if 3 > escolha > -1: 
    computador = random.randint(0,2)
    itens = ['Pedra', 'Papel','Tesoura']
    print(f'O computador escolheu {itens[computador]}' )
    print(f'Você escolheu {itens[escolha]}') 
    #EMPATES
    if escolha == 0 and computador == 0:
        print('EMPATE!')
    elif escolha == 1 and computador == 1:
        print('EMPATE!')
    elif escolha == 2 and computador == 2:
        print('EMPATE!')

    #VITORIAS JOGADOR
    elif escolha == 0 and computador == 2:
        print('Você VENCEU!')
    elif escolha == 1 and computador == 0:
        print('Você VENCEU!')
    elif escolha == 2 and computador == 1:
        print('Você VENCEU!')
    
    #VITORIAS COMPUTADOR
    elif escolha == 0 and computador == 1:
        print('Você perdeu')
    elif escolha == 1 and computador == 2:
        print('Você perdeu')
    elif escolha == 2 and computador == 0:
        print('Você perdeu')
else: print('Escolha do jogador invalida!')



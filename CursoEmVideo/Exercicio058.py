'''58 Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
 Só que agora o jogador vai tentar adivinhar até acertar, 
 mostrando no final quantos palpites foram necessários para vencer.'''

import random

print("Vou pensar em um número entre 0 e 10. Tente adivinhar...")
usuario = int(input("Qual número eu vou escolher? "))
print("Processando...")

tentativas = 1
computador = int(random.randint(0,10))
if usuario != computador:
    print(f"Você errou o número escolhido foi: {computador}")
    while not usuario == computador:
            usuario = int(input("Qual número eu vou escolher? "))
            tentativas += 1
            print(f"Você errou o número escolhido foi: {computador}")
            computador = int(random.randint(0,10))

print(f"Parabêns você acertou! O número escolhido foi {computador}")
print(f'Foram necessárias {tentativas} tentativas')
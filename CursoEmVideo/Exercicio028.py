'''28 Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5,
 peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
  O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

import random
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
usuario = int(input("Qual número eu vou escolher? "))
print("Processando...")
computador = int(random.randint(0,5))

if usuario == computador:
    print(f"Parabêns você acertou! O número escolhido foi {computador}")
else:
    print(f"Você errou o número escolhido foi: {computador}")


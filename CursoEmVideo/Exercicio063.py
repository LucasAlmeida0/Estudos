#63  Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
termos = int(input('Quantos termos você quer mostrar? '))
termo1 = 0
termo2 = termo3 = 1
atual = termos
while termos > 0:
    if termos == 2:
        print(f'{termo1} → {termo2}', end='→')
    elif termos == 1:
        print(f'{termo1}', end ='→')
    else:
        termo3 = termo1 + termo2
        print(termo3, end=' → ')
        atual -= 1
        termo1 = termo2
        termo2 = termo3
print('FIM')

    

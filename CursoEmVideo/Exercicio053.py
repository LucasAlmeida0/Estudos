'''53 Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. '''

frase = str(input('Digite uma frase: ')).replace(' ', '').upper()
print(f'O inverso de {frase} é {frase[::-1]}')
if frase == frase[::-1]:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

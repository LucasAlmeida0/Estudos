'''74 Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, 
mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

from random import randint
numeros = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print(f'Os valores sorteados foram {numeros[0]}  {numeros[1]}  {numeros[2]}  {numeros[3]}  {numeros[4]}')
print(f'O maior valor sorteado foi {max(numeros)}')
print(f'O menor valor foi sorteado {min(numeros)}')
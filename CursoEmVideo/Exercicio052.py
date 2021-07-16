#52 Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
contador = 0
numero = int(input('Digite um número: '))
x = numero
for x in range(1,numero+1):
    if numero % x == 0:
        contador += 1

print(f'O número {numero} foi divisível {contador} vezes')
if contador == 2:
    print(f'E por isso ele É PRIMO!')
else: 
    print(f'E por isso ele NÃO É PRIMO!')
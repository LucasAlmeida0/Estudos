'''64 Crie um programa que leia vários números inteiros pelo teclado.
      O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
      No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''
numero = 0
soma = 0
contador = 0
while numero != 999:
    contador += 1
    soma += numero
    numero = int(input('Digite um número [999 para parar]: '))
print(f'A soma de todos os {contador-1} números digitados é {soma}')

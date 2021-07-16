'''65 Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
      mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
      O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
contador = 1
continuar = str
numero = int(input('Digite um número: '))
soma = numero
maior = menor = numero
continuar = str(input('Deseja continuar? [S/N]')).upper().split() [0]
while not continuar in 'N':
    numero = int(input('Digite um número: '))
    soma += numero
    contador  += 1
    continuar = str(input('Deseja continuar? [S/N]')).upper().split() [0]
    if maior < numero: maior = numero
    elif menor > numero: menor = numero
print(f'Foram digitados {contador} números que somam {soma} e a média da {soma/contador:.2f}')
print(f'O maior número é {maior} e o menor é {menor}')
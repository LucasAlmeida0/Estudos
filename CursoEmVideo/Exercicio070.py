'''70 Crie um programa que leia o nome e o preço de vários produtos.
 O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''
total = produtos = menor = 0
while True:
    nome = str(input('Nome do produto: '))
    preço = int(input('Preço: '))
    if preço > 1000: produtos += 1
    if menor > preço or total == 0:
        barato = nome
        menor = preço
    total += preço
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar in 'N': break
print(f'Total a pagar: R${total:.2f}')
print(f'Produtos acima de R$1.000,00: {produtos} ')
print(f'O produto mais barato é {barato}')
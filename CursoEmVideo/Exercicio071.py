'''71  Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado 
(número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''
print('='*20)
print('    BANCO LUCAS    ')
print('='*20)
sacado = float(input('Digite o valor a ser sacado:R$'))
cinquenta = vinte = dez = um = resto = 0
while True:
    cinquenta = sacado / 50
    resto = sacado % 50
    if resto == 0: break
    vinte = resto / 20
    resto = resto % 20
    if resto == 0:  break
    dez = resto / 10
    resto = resto % 10
    if resto == 0: break
    um = resto / 1
    break
print(f'Total de {cinquenta:.0f} cédulas de R$50')
print(f'Total de {vinte:.0f} cédulas de R$20')
print(f'Total de {dez:.0f} cédulas de R$10')
print(f'Total de {um:.0f} cédulas de R$1')




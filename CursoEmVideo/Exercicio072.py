'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

numeros = ('zero', 'um', 'dois','três','quatro','cinco', 'seis', 'sete','oito','nove','dez','onze','doze','treze','quatorze','quinze',
'dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    escolhido = int(input('Digite um número de 1 a 20: '))
    while True:
        if escolhido >= 0 and escolhido <= 20: break
        escolhido = int(input('Número errado, Tente novamente! Digite um número de 1 a 20: '))
    print(f'Você digitou o número {numeros[escolhido]}')
    continuar = str(input('Deseja Continuar? [S/N] ')).upper()[0]
    if continuar in 'N': break
        
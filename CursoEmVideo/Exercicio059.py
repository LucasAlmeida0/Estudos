'''59 Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar [ 2 ] multiplicar [ 3 ] maior [ 4 ] novos números [ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
numero1 = int(input("Digite o primeiro valor: "));
numero2 = int(input("Digite o segundo valor: "));
print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
escolha = int(input('Qual é sua escolha? '))

while escolha != 5:

    if escolha == 1:
        print('-----------------------')
        print(f"{numero1} + {numero2} = {numero1+numero2}");
        print('-----------------------')
    if escolha == 2:
        print('-----------------------')
        print(f"{numero1} * {numero2} = {numero1*numero2}");
        print('-----------------------')
    if escolha == 3:
        if numero1 > numero2:
            print('-----------------------')
            print(f"O maior é {numero1}")
            print('-----------------------')
        else:
            print('-----------------------')
            print(f'O maior é {numero2}')
            print('-----------------------')
    if escolha == 4:
        print('-----------------------')
        numero1 = int(input("Digite o primeiro valor: "))
        numero2 = int(input("Digite o segundo valor: "))
        print('-----------------------')
    escolha = int(input('Qual é sua escolha? '))

'''67 Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
  O programa será interrompido quando o número solicitado for negativo.'''
while True:
    num = int(input('Qual número você deseja ver a tabuada: '))
    if num < 0: break
    print(f'TABUADA do {num}')
    print('-*'*10)
    for c in range(0,11):
        print(f'{num} x {c} = {num * c}')
    print('-*'*10)

print('PROGRAMA TABUADA ENCERRADO! Volte Sempre!')
    

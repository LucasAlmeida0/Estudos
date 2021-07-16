'''51 Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, 
 mostre os 10 primeiros termos dessa progressão.'''

razão = int(input('Digite o valor da razão: '))
primeiro_termo = int(input('Digite o valor do primeiro termo: '))
resultado = primeiro_termo 
print(primeiro_termo, end=' → ')
for c in range(0,9):
    resultado += razão
    print(resultado, end=' → ')
print('ACABOU')


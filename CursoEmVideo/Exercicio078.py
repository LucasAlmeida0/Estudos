'''78 Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
 No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''
valores = list()
posicao_maior = list()
posicao_menor = list()
for c in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
for c, v in enumerate(valores):
    if v == max(valores):
        posicao_maior.append(c)
        print(posicao_maior)
    if v == min(valores):
        posicao_menor.append(c)
        print(posicao_menor)
print(f'Você digitou os valores: {valores} ')

print(f'O maior valor digitado foi {max(valores)} nas posições ', end = '')
for v in posicao_maior:
    print(f'{v}', end='...')

print(f'\nO menor valor digitado foi {min(valores)} nas posições ', end='')
for m in posicao_menor:
   print(f'{m}', end='...')




'''61 Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''
primeiro_termo = (int(input('Primeiro Termo: ')))
r = int(input('Razão: '))
contador = 1
soma = primeiro_termo
print(primeiro_termo, end=' → ')
while contador != 10:
    soma += r
    contador +=1
    print(soma, end= '') 
    if contador != 10 : print(end=' → ')
        
    
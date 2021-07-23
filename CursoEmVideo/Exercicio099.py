from time import sleep
def maior(*n):
    maior  = 0
    contador = 0
    print('Analisando os valores passados...')
    for valor in n:
        print(f'{valor}',end=' ',flush=True)   
        sleep(0.3)
        if contador == 0 or maior < valor:
            maior = valor
        contador += 1
    print(f'\nForam informado {contador} valores ao todo')
    print(f'O maior valor informado foi {maior}')
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
from  random import randint
numeros = list()

def sorteia():
    print('Sorteando 5 valores da lista: ', end=' ')
    for c in range(0,5):
        sorteado = randint(0,10)
        print(sorteado, end=' ')
        numeros.append(sorteado)
    print('Pronto!')
    

def somaPar(list):
    soma = 0
    for k, c in enumerate(list):
        if c % 2 == 0:
            soma += c
    print(f'somando os valores de pares {numeros}, temos {soma}')


sorteia()
somaPar(numeros)



from time import sleep

def contador(inicio, fim, passo):
    print('-='*30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if passo == 0: passo = 1
    if inicio < fim:
        if passo < 0: passo = -(passo)
        for c in range(inicio,fim+1, passo):
            print(c, end =' ',flush=True)
            sleep(0.5)
        print('Fim')
    elif inicio > fim:
        if passo > 0: passo = -(passo)
        for c in range(inicio,fim-1, passo):
            print(c, end =' ',flush=True)
            sleep(0.5)
        print('Fim')

contador(1,10,1)
contador(10,0,2)

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)
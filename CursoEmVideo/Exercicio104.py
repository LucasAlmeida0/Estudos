def leiaint(texto):
    while True:
        n= str(input(texto))
        if n.isnumeric():break
        else: print('ERRO!  Digite um número inteiro valido')
    return n


num = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {num}')
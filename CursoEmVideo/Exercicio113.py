def leiaint(texto):
    try:
        n= str(input(texto))
        if n.isnumeric:
         return int(n)
    except:
        print('cu')

def leiafloat():
    print('cu')

inteiro = leiaint('Digite um número inteiro: ')
#real = leiafloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {inteiro}')

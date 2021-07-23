def escreva(texto):
    tamanho = len(texto) + 4
    print('~'* tamanho)
    print(f' {texto}')
    print('~'* tamanho)

texto = str(input('Digite o texto desejado:'))
escreva(texto)
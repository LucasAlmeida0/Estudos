def escreva(texto):
    tamanho = len(texto) + 9
    print('-'* tamanho)
    print(texto)
    print('-'* tamanho)

texto = str(input('Digite o texto desejado:'))
escreva(texto)
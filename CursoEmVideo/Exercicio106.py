def escreva(texto):
    tamanho = len(texto) + 4
    print('~'* tamanho)
    print(f' {texto}')
    print('~'* tamanho)


def sistemaajuda(texto):
    while True:
        if texto.upper().strip() == 'FIM': break
        escreva(F'ACESSANDO O MANUAL DO COMANDO {texto}')
        help(texto)
        escreva('SISTEMA DE AJUDA PyHelp')
        texto = str(input('Função da Biblioteca > ')).strip()



escreva('SISTEMA DE AJUDA PyHelp')
entrada = str(input('Função da Biblioteca > '))
sistemaajuda(entrada)
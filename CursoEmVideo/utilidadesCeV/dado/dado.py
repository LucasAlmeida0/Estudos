def leiadinheiro(texto):
    valido = False
    while not valido:
        entrada = str(input(texto)).replace(',','.').strip()
        if entrada.isalpha or entrada == '':
            print(f'ERRO! "{entrada}" é não é um número valido')
        else:
            valido = True
            return float(entrada)
       
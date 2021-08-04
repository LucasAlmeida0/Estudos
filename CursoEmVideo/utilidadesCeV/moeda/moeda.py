def aumentar(valor_aumentar, aliquota_aumentar, formatar_aumentar = False):
    '''
    -> Aumenta o valor pela aliquota
    :param valor_aumentar: Valor a ser aumentado
    :param aliquota_aumentar: Porcentagem a aumentar
    :param formatar: Formatar ou não o valor retornado para moeda
    :return: valor aumentado
    '''
    resultado_aumentar = valor_aumentar + valor_aumentar * (aliquota_aumentar/100)
    if formatar_aumentar:
        return moeda(resultado_aumentar)
    else:
        return resultado_aumentar

def diminuir(valor_diminuir, aliquota_diminuir, formatar_diminuir = False):

    '''
    -> Diminui o valor pela aliquota
    :param valor_diminuir: Valor a ser diminuído
    :param aliquota_diminuir: Porcentagem a diminuir
    :param formatar: Formatar ou não o valor retornado para moeda
    :return: valor diminuído
    '''
    resultado_diminuir = valor_diminuir - valor_diminuir * (aliquota_diminuir/100)
    if formatar_diminuir:
        return moeda(resultado_diminuir)
    else: 
        return resultado_diminuir

def metade(valor_metade, formatar_metade = False):
    '''
    -> Retorna a metade do valor
    :param valor_metade: Valor a dividir
    :param formatar: Formatar ou não o valor retornado para moeda
    :return: Resultado de valor_metade dividido por 2
    '''
    resultado_metade = valor_metade/2
    if formatar_metade:
        return moeda(resultado_metade)
    else:
        return resultado_metade

def dobro(valor_dobro, formatar_dobro = False):
    '''
    -> Retorna o valor dobrado
    :param valor_dobro: Valor que será dobrado
    :param formatar: Formatar ou não o valor retornado para moeda
    :return: Resultado do valor vezes dois
    '''
    resultado_dobro = valor_dobro * 2
    if formatar_dobro:
        return moeda(resultado_dobro)
    else:
        return resultado_dobro

def moeda(valor_moeda):


    '''
    -> Formata o valor para moeda
    :param valor_moeda: Valor a ser formatado
    :return: Valor formatado
    '''
    resultado_moeda = str(f'R$ {valor_moeda:.2f}')
    resultado_moeda = resultado_moeda.replace('.',',' )
    return resultado_moeda

def resumo(valor_resumo, aliquota_resumo_aumentar,aliquota_resumo_diminuir):

    escreva('RESUMO DO VALOR')
    print(f'Preço analisado:{moeda(valor_resumo):>47}')
    print(f'Dobro preço: {moeda(dobro(valor_resumo)):>50}')
    print(f'Metade do Preço: {moeda(metade(valor_resumo)):>45}')
    print(f'{aliquota_resumo_aumentar}% de juros: {moeda(aumentar(valor_resumo, aliquota_resumo_aumentar)):>49}')
    print(f'{aliquota_resumo_diminuir}% de desconto: {moeda(diminuir(valor_resumo, aliquota_resumo_diminuir)):>45}')
    escreva('FIM DO PROGRAMA')


def escreva(texto):
    tamanho = len(texto) + 50
    print('~'* tamanho)
    print(f' {texto}')
    print('~'* tamanho)
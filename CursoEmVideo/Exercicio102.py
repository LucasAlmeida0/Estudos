def fatorial(produto, show=False):
    '''
    => Calcula o fatorial de um numero.
    :param produto: Número a ser calculado
    :param show: (opcional) Mostrar ou não a conta.
    :return: variavel resultado que será equivalente ao fatorial do produto
    '''
    resultado = produto
    resposta = str(f'{resultado}! = ')
    
    if show:
        for c in range(0,produto):
            if c < produto-1:
                resultado += resultado * c
            if produto - c != 1:
                resposta += f'{produto-c} x '
            else:
                resposta += f'{produto-c} = {resultado}' 
        return resposta
    else:
        for c in range(1,produto-1):
            resultado += resultado * c
        return resultado

print(fatorial(1,show=True))
help(fatorial)


valores = list()
while True:
    valor_atual = int(input('Digite um valor: '))
    if  valor_atual in valores:
        print('Valor duplicado! Não vou adicionar...')
        
    else:
        print('Valor adicionado com sucesso...')
        valores.append(valor_atual)
        print(valores)
    
    continuar = str(input('Deseja continuar?[S/N]')).upper().strip()[0]
    if continuar in 'N': break
valores.sort()
print('-' * 30)
print(f'Você digitou os valores {valores}')
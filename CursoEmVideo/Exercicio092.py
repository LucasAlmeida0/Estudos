from datetime import date
dados = dict()
dados['nome'] = str(input('Nome: '))
dados['idade'] = int(input('Ano de nascimento: '))
dados['ctps'] = int(input('Carteira de trabalho: [0 não tem]'))

atual = date.today().year
dados['idade'] =  (atual - dados['idade']) 
if dados['ctps'] != 0:

    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = int(input('Salário: R$'))
    dados['aposentadoria'] = int((atual - dados['contratação']) + 35)
    #}


print(dados)
for k, v in enumerate(dados):
    print(f'{v} tem o valor {dados[v]}')
    



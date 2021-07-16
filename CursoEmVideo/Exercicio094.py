pessoa = dict()
lista_de_pessoas = list()
total_idade = 0
mulheres = list()
pessoas_acima_da_media = list()

while True:
    pessoa['nome'] = str(input('Nome:')).strip()
    pessoa['sexo'] = str(input('Sexo:')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    total_idade += pessoa['idade']
    if pessoa['sexo'] in 'F': mulheres.append(pessoa['nome'])
    lista_de_pessoas.append(pessoa.copy())
    del pessoa['idade'], pessoa['nome'],pessoa['sexo']
    continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if continuar in 'N': break

print('-'*30)
print(f'O grupo tem {len(lista_de_pessoas)} pessoas')
print(f'A média de idade é de {total_idade/len(lista_de_pessoas):.2f}')
print(f'As mulheres cadastradas foram', end=': ')
for k,v in enumerate(mulheres):
    if k == len(mulheres): 
        print(mulheres[k])
        break
    print(mulheres[k],end=' -> ')
print('ACABOU')
print('Lista das pessoas que estão acima da média: ')
for c in range(0,len(lista_de_pessoas)):
    if lista_de_pessoas[c]['idade'] > total_idade/len(lista_de_pessoas):
        print(f'Nome: {lista_de_pessoas[c]["nome"]}', end=' ')
        print(f'Sexo: {lista_de_pessoas[c]["sexo"]}', end=' ')
        print(f'Idade: {lista_de_pessoas[c]["idade"]}')


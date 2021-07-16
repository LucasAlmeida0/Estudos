'''56 Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, 
mostre: a média de idade do grupo, 
 qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''

media, jovem, velho = 0,0,0
for c in range (1,5):
    print(f'--------{c}ª PESSOA---------')
    nome = str(input(f'Nome: ')).strip()
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo [M/F]: ')).upper().strip()
    media += idade
    if sexo == 'M':
        velho_nome = nome
        velho_idade = idade
    elif sexo == 'F' and idade < 20:
        jovem += 1
print(f'A média de idade do grupo foi de {media/4}')
print(f'O homem mais velho tem {velho_idade} anos e se chama {velho_nome}')
print(f'Ao todo são {jovem} mulheres com menos de 20 anos')


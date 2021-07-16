'''69 Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, 
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''
maior = homens = mulheres = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if idade >= 18: maior += 1
    if sexo in 'M': homens +=1
    if sexo in 'F' and idade < 20: mulheres += 1
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar in 'N': break
print(f'Maiores de idade: {maior}')
print(f'Homens: {homens} ')
print(f'Mulheres com menos de 20 anos: {mulheres}')

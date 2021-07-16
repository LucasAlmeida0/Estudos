''' 54 Crie um programa que leia o ano de nascimento de sete pessoas. 
 No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
import datetime
atual = datetime.date.today().year
nascimento, maior , menor , idade = 0, 0 , 0 ,0

for c in range(0,7):
    nascimento = int(input("Ano de nascimento: "))
    idade = atual - nascimento
    if idade >= 18:
       maior += 1
    else:
        menor += 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade')
print(f'E também tivemos {menor} pessoas menores de idade')
        

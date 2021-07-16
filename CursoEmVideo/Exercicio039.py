'''39 Faça um programa que leia o ano de nascimento de um jovem e informe,de acordo com a sua idade, 
 se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
 Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
import datetime
sexo = str(input('Digite seu sexo: Masculino(M) ou Feminino(F) ')).strip().upper()
if sexo == 'M':
    atual = datetime.date.today().year
    nascimento = int(input("Ano de nascimento: "))
    idade = atual - nascimento
    if idade < 18:
        print(f"Quem nasceu em {nascimento} tem {idade} anos em {atual}")
        print(f"Ainda faltam {18 - idade} anos para o alistamento")
        print(f'Seu alistamento será em {(18 - idade) + atual}')
    elif idade > 18:
        print(f'Quem nasceu em {nascimento} tem {idade} anos em {atual}')
        print(f'Você deveria ter se alistado há {idade - 18} anos')
        print(f'Seu alistamento foi em {-(idade - 18 - atual)}')
    else:
        print(f'Quem nasceu em {nascimento} tem {idade} anos em {atual}')
        print(f'Você precisa se alistar IMEDIATAMENTE')
elif sexo == 'F':
    print("No Brasil o alistamento militar é obrigatório somente para homens")
else:
    print("Sexo invalido, tente novamente")


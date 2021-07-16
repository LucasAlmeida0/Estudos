'''34 Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
 Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, 
 o aumento é de 15%.'''

salario = float(input("Digite o seu sálario: "))

if salario > 1250:
    print(f'O seu novo salário é {salario + salario * 0.10}')
else:
    print(f'O seu novo salário é {salario + salario * 0.15}')
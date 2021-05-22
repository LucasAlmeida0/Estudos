#8 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

Salario = int(input("Quanto você ganha por hora?: "));
Horas = int(input("Quantas horas você trabalha no mês?: "));

SalarioMensal = Salario * Horas;

print("Seu salario mensal é {}".format(SalarioMensal));
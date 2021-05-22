"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, 
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido."""


Ganho = float(input("Digite o quanto você ganha por hora: "));
Horas = int(input("Digite quantas horas você trabalha no mês: "));

SalarioBruto = Ganho * Horas;
Ir = SalarioBruto - (SalarioBruto * 11 / 100);
Inss = SalarioBruto - (SalarioBruto * 8 / 100);
Sindicato = SalarioBruto - (SalarioBruto * 5 / 100);
SalarioLiquido = SalarioBruto - (SalarioBruto * 11 / 100) - (SalarioBruto * 8 / 100) - (SalarioBruto * 5 / 100);

print("""Salário Bruto : R${}
 IR (11%) : R${}
INSS (8%) : R${}
Sindicato ( 5%) : R${}
Salário Liquido : R${}""".format(SalarioBruto,Ir,Inss,Sindicato,SalarioLiquido));
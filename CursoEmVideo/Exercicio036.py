'''36 Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa
 o salário do comprador e em quantos anos ele vai pagar.
 A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado'''

valor = float(input("Digite o valor da casa:R$"))
salario = int(input("Quanto é o seu salário?R$"))
anos = int(input("Em quantos anos você pretende pagar? "))


print(f'Para pagar uma casa de R${valor:.2f} em {anos} anos a prestação mensal será de R${(valor/anos)/12} ')
if (valor/anos)/127 > salario * 0.30:
    print("Empréstimo NEGADO!")
else:
    print("Empréstimo CONCEDIDO!")





 
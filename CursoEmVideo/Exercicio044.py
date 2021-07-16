'''44 Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros'''
preco = float(input('Preço da Compra: R$'))
print('''FORMAS DE PAGAMENTO
[1] á vista dinheiro/cheque
[2] á vista no cartão
[3] 2X no cartão
[4] 3X ou mais no cartão''')
pagamento = int(input("Qual é a opção? "))
print(f"O preço original da compra será: R${preco:.2f}")
if pagamento == 1:
    print("Você ganhou um desconto de 10%")
    print(f"O preço que você deverá pagar é: R${preco - preco * 0.10}")
elif pagamento == 2:
    print("Você ganhou um desconto de 5%")
    print(f"O preço que você deverá pagar é: R${preco - preco * 0.05}")
elif pagamento == 3:
    print("Não houve mudanças no preço!")
    print(f"O preço que você deverá pagar é: R${preco}")
elif pagamento == 4:
    print("Você pagará com juros de 20%")
    print(f"O preço que você deverá pagar é: R${preco + preco * 0.20}")
else:
    print("Forma de pagamento invalida!")
    


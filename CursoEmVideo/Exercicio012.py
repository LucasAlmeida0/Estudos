#12 Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input("Digite o preço: R$ "))
print(f"Preço: R$ {preco}")
print(f"Preço com desconto: R$ {preco - preco * 0.05}")
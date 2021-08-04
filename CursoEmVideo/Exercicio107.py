from utilidadesCeV import moeda

preco = float(input('Digite o preço: R$'))
porcentagem = float(input('Digite a aliquota:'))
print(f'A metade de R${preco:.2f} é R${moeda.metade(preco):.2f}')
print(f'O dobro de R${preco:.2f} é R${moeda.dobro(preco):.2f}')
print(f'Aumentando R${preco:.2f} em {porcentagem}% temos R${moeda.aumentar(preco, porcentagem):.2f}')
print(f'Diminuindo R${preco:.2f} em {porcentagem}% temos R${moeda.diminuir(preco, porcentagem):.2f}')


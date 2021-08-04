from utilidadesCeV import moeda


preco = float(input('Digite o preço: R$'))
porcentagem = float(input('Digite a aliquota:'))
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'Aumentando {moeda.moeda(preco)} em {porcentagem}% temos {moeda.aumentar(preco, porcentagem, True)}')
print(f'Diminuindo {moeda.moeda(preco)} em {porcentagem}% temos {moeda.diminuir(preco, porcentagem, True)}')

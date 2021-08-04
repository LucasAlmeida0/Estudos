from utilidadesCeV import moeda


preco = float(input('Digite o preço: R$'))
porcentagem = float(input('Digite a aliquota:'))
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
print(f'Aumentando {moeda.moeda(preco)} em {porcentagem}% temos {moeda.moeda(moeda.aumentar(preco, porcentagem))}')
print(f'Diminuindo {moeda.moeda(preco)} em {porcentagem}% temos {moeda.moeda(moeda.diminuir(preco, porcentagem))}')

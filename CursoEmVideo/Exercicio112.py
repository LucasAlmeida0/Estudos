from utilidadesCeV.dado import dado
from utilidadesCeV.moeda import moeda
p = 'Digite o preço: R$'
p = dado.leiadinheiro(p)
moeda.resumo(p,10,10)
galera = list()
dados = list()
maior = list()
menor = list()

contador = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    galera.append(dados[:])
    dados.clear()
    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if continuar in 'N': break

print('-' * 15)

for p in galera:
    contador +=1
    if  contador == 1:
        maior.append(p[0])
        menor.append(p[0])
        menor.append(p[1])
        maior.append(p[1])
    elif p[1] >= maior[1]:
        if p[1] > maior[-1]: maior.clear()
        maior.append(p[0])
        maior.append(p[1])
    elif p[1] <= menor[1]:
        if p[1] < menor[-1]: menor.clear()
        menor.append(p[0])
        menor.append(p[1])


print(f'Ao todo você cadastrou {contador} pessoas')
print(f'O maior peso foi de {maior[1]:.2f}kg. Peso de {maior[0::2]}')
print(f'O menor peso foi de {menor[1]:.2f}kg. Peso de {menor[0::2]}')
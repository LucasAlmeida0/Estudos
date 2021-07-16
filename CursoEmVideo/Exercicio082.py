valores = list()
pares = list()
impares = list()
while True:
    valores.append(int(input('Digite um número: ')))
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar in 'N': break

for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print(f'Lista total: {valores}')
print(f'Pares: {pares}')
print(f'Impares: {impares}')

valores = list()
teste = 0
while True:
    valores.append(int(input('Digite um número: ')))
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar in 'N': break

print(f'Foram digitados {len(valores)} números')
valores.sort(reverse=True)
print(f'Os valores em ordem descrente são {valores}')
for v in valores:
    if v == 5:
        print('O valor 5 faz parte da lista!')
        teste = v
        break
if teste == 0:
    print('O valor 5 não faz parte da lista!')
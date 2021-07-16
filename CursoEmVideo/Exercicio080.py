
valores = [int(input('Digite um valor: '))] 

valor2 = int(input('Digite um valor: ')) 

if valor2 >= valores[0]:
    valores.insert(1, valor2)
    print('Adicionado ao final da lista')
else:
    valores.insert(0, valor2)
    print('Adicionado na posição 0 da lista')

valor3 = int(input('Digite um valor: ')) 
if valor3 >= valores[-1]:
    valores.append(valor3)
    print('Adicionado ao final da lista...')
elif valor3 >= valores[0]:
    valores.insert(1, valor3)
    print('Adicionado a posição 1 da lista...')
else:
    valores.insert(0, valor3)
    print('Adicionado a posição 0 da lista...')

valor4 = int(input('Digite um valor: '))
if valor4 <= valores[0]:
    valores.insert(0,valor4)
    
elif valor4 <= valores[1]:
    valores.insert(1,valor4)
elif valor4 <= valores[2]:
    valores.insert(2,valor4)
else:
    valores.append(valor4)
    print('Adicionado ao final da lista')

valor5 = int(input('Digite um valor: '))
if valor5 <= valores[0]:
    valores.insert(0,valor5)
elif valor5 <= valores[1]:
    valores.insert(1,valor5)
    print('Adicionado a posição 1 da lista...')
elif valor5 <= valores[2]:
    valores.insert(2,valor5)
    print('Adicionado a posição 2 da lista...')
elif valor5 <= valores[3]:
    valores.insert(3, valor5)
    print('Adicionado a posição 3 da lista...')
    
else:
    valores.append(valor5)
    print('Adicionado ao final da lista')

print(f'Os valores digitados em ordem são {valores}')
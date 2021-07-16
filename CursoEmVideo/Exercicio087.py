matriz = [ [ [], [], [] ], 
          [ [], [], []], 
          [ [], [], []]]

soma = 0
soma_terceira = 0
maior = 0

for l in range(0,3):
    for c in range(0,3):
        num = int(input(f'Digite um valor para [{l}, {c}]: '))
        matriz[l][c].append(num)
        if num % 2 == 0:
            soma += num
        if c == 2:
            soma_terceira += num
        if l == 1 and maior < num or l == 1 and c == 0:
            maior = num
        
print('-'*15)
print(matriz[0][0:3])
print(matriz[1][0:3])
print(matriz[2][0:3])
print('-'*15)

print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores da terceira coluna é {soma_terceira}')
print(f'O maior valor da segunda linha é {maior}')

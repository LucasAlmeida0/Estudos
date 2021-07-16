matriz = [ [ [], [], [] ], 
          [ [], [], []], 
          [ [], [], []]]

for p in range(0,3):
    for c in range(0,3):
        num = int(input(f'Digite um valor para [{p}, {c}]: '))
        matriz[p][c].append(num)

print(matriz[0][0:3])
print(matriz[1][0:3])
print(matriz[2][0:3])
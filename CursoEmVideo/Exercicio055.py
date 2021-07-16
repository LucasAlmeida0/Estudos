#55 Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
peso, menor, maior = 0, 0, 0
for c in range(1, 6):
    peso = float(input(f"Digite o peso da {c}ª pessoa: "))
    if peso > maior:
        maior = peso
    if peso < menor or menor == 0:
        menor = peso

print(f'O maior peso lido foi {maior:.2f} Kg')
print(f'O menor peso lido foi {menor:.2f} Kg')
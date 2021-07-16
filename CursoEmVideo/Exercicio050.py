'''50 Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
 Se o valor digitado for ímpar, desconsidere-o.'''
soma = 0
contador =0 
for c in range(1,7):
    numero = int(input(f"Digite o {c}° número: "))
    if numero % 2 == 0:
        contador += 1
        soma += numero
print(f'Você informou {contador} números PARES e a soma é {soma}')
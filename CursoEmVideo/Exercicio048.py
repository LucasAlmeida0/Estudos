#48 Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
contador = 0
for c in range(0,501, 3):
    if c % 2 != 0 and c < 500:
        contador += 1
        soma += c    
print(f'A soma dos {contador} números é {soma}')


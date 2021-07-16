#60 Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

numero = int(input('Digite um número: '))
resultado = numero
print(f'Calculando {numero}! = {numero}',end=' ' )
while numero != 1:    
    numero -= 1
    print(f' x {numero}', end=' ')
    resultado = resultado * numero

print(f'= {resultado}')
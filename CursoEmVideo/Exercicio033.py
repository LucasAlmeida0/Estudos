#33 Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))

menorvalor = 0 
maiorvalor = 0

if valor1 < valor2 and valor1 < valor3:
    menorvalor = valor1
elif valor2 < valor1 and valor2 < valor3:
    menorvalor = valor2
elif valor3 < valor1 and valor3 < valor2:
    menorvalor = valor3

if valor1 > valor2 and valor1 > valor3:
    maiorvalor = valor1
elif valor2 > valor1 and valor2 > valor3:
    maiorvalor = valor2
elif valor3 > valor1 and valor3 > valor2:
    maiorvalor = valor3

print(f"O menor valor digitado foi {menorvalor}")
print(f"O maior valor digitado foi {maiorvalor}")
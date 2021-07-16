#35 Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

primeira_reta = float(input("Digite o valor da primeira reta"))
segunda_reta = float(input("Digite o valor da segunda reta"))
terceira_reta = float(input("Digite o valor da terceira reta"))

if primeira_reta < segunda_reta + terceira_reta and segunda_reta < primeira_reta + terceira_reta and terceira_reta < primeira_reta + segunda_reta:
    print("Os segmento acima podem formar um triângulo")
else:
    print("Os segmento acima podem NÃO formar um triângulo")
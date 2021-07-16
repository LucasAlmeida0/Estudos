'''42 Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes'''

primeira_reta = float(input("Digite o valor da primeira reta"))
segunda_reta = float(input("Digite o valor da segunda reta"))
terceira_reta = float(input("Digite o valor da terceira reta"))

if primeira_reta < segunda_reta + terceira_reta and segunda_reta < primeira_reta + terceira_reta and terceira_reta < primeira_reta + segunda_reta:
    if primeira_reta  == segunda_reta == terceira_reta:
        print("Os segmento acima podem formar um triângulo EQUILÁTERO")
    elif primeira_reta != segunda_reta != terceira_reta != primeira_reta:
        print("Os segmento acima podem formar um triângulo ISÓSCELES")
    else:
        print("Os segmento acima podem formar um triângulo ISÓSCELES")


else:
    print("Os segmento acima podem NÃO formar um triângulo")
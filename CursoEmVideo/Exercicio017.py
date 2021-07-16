'''17 Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
 Calcule e mostre o comprimento da hipotenusa.'''
import math
cateto_oposto = float(input("Digite o valor do cateto oposto: "))
cateto_adjacente = float(input("Digite o valor do cateto adjacente"))
hipotenusa = cateto_oposto * cateto_oposto + cateto_adjacente * cateto_adjacente

print(f"O valor da hipotenusa é {math.sqrt(hipotenusa)}")

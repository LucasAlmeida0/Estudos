#18 Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

angulo = float(input("Digite um valor de ângulo: "))
print(f"O ângulo de {angulo:.2f} tem o Seno de  {math.sin(math.radians(math.ceil(angulo))):.2f}")
print(f"O ângulo de {angulo:.2f} tem o  de  {math.cos(math.radians(math.ceil(angulo))):.2f}")
print(f"O ângulo de {angulo:.2f} tem o Tangente de  {math.tan(math.radians(math.ceil(angulo))):.2f}")

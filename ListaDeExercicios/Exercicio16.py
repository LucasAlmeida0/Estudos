"""Faça um programa para uma loja de tintas.
 O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
 Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total."""

Tamanho = float(input("Digite o tamanho em m²: "));

Litros = Tamanho/3; 
Baldes = int(Litros/18)
Custo = Baldes*80

print("Pintar {}m² exigira {} L que totaliza {} baldes e custara no total R${:.2F}".format(Tamanho,Litros,Baldes,Custo));


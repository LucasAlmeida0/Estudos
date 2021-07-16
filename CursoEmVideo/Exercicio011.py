''' 11 Faça um programa que leia a largura e a altura de uma parede em metros, 
calcule a sua área e a quantidade de tinta necessária para pintá-la, 
 sabendo que cada litro de tinta pinta uma área de 2 metros quadrados. '''

largura = float(input("Digite a largura: "))
altura = float(input("Digite a altura: "))
area = largura*altura
quantidade_de_tinta = int(area/2)
print(f"Você precisará de {quantidade_de_tinta} lata de tinta para pintar {area}m")


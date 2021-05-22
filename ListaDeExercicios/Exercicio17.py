"""Faça um Programa para uma loja de tintas.
 O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
 Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
 que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. 
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias."""

Metros = float(input("Digite o tamanho em m²: "));
Cobertura = Metros/6 + Metros*10/100;

Latas = int(Cobertura/18);
CustoLatas = float(Latas*80);

Galoes = int(Cobertura/3.6);
CustoGaloes = float(Galoes*25);

Resto = float(Cobertura%18);
RestoGaloes = int(Resto/3.6);
CustoRestoGaloes = RestoGaloes*25;

print("""
Quantidade de tinta necessária:{}L
Comprar apenas latas de 18L  
    Latas: {}
    Preço: R${:.2f}

Comprar apenas galões de 3,6L:
    Galões: {}
    Preço: R${:.2f}

Misturar latas e galões:
    Latas: {}
    Galões: {}
    Preço das Latas: R${:.2f}
    Preço dos Galoes: R${:.2f}
""".format(Cobertura,Latas+1,CustoLatas,Galoes+1,CustoGaloes,Latas,RestoGaloes,CustoLatas,CustoRestoGaloes))


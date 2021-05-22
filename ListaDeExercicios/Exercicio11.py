""" Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
        A.  O produto do dobro do primeiro com metade do segundo .
        B.  A soma do triplo do primeiro com o terceiro.
        C.  O terceiro elevado ao cubo."""

n1 = int(input("Digite um número inteiro: "));
n2 = float(input("Digite um número real: "));

a = (n1*2) + (n2/2);
b = (n1*3) + a;
c = a*a*a;

print("A = {}, B = {}, C = {}".format(a,b,c));





 
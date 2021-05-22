""" Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
        Para homens: (72.7*h) - 58
        Para mulheres: (62.1*h) - 44.7"""

h = float(input("Digite sua altura: "));

homens = (72.7*h) - 58;
mulheres = (62.1*h) - 44.7;

print("Com a altura {:.2f} seu peso ideal caso homem é {:.2f}, caso seja mulher {:.2f}".format(h,homens,mulheres));


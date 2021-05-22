# 12 Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

Altura = float(input("Digite sua altura: "));
PesoIdeal = ( 72.7 * Altura ) - 58;

print("Seu peso ideal é {:.2f}".format(PesoIdeal));

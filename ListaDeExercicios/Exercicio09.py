# 9 Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

F = float(input("Digite a temperatura em °F:"));

C = 5 * ((F-32) / 9);

print("{}°F equivale a {:.2f}°C ".format(F, C));
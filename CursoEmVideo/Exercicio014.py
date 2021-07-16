#14 Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

Celsius = float(input("Digite  uma temperatura em °C:  "))
Fahrenheit = Celsius * 9/5 + 32

print(f" {Celsius:.2f} °C é equivalente a {Fahrenheit:.2f} °F ")
'''27 Faça um programa que leia o nome completo de uma pessoa,
 mostrando em seguida o primeiro e o último nome separadamente.'''

nome = str(input("Digite seu nome: ")).strip()
primeiro = nome.find(" ")
ultimo = nome.rfind(" ")
print(f"Seu primeiro nome é: {nome[:primeiro]}")
print(f"Seu último nome é: {nome[ultimo:]}")
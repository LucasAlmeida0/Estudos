'''29 Escreva um programa que leia a velocidade de um carro.
 Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
A multa vai custar R$7,00 por cada Km acima do limite.'''

velocidade = int(input("Digite a velocidade: "))

if velocidade <= 80:
    print("Tenha um bom dia! Dirija com segurança!")
else:
    print("MULTADO! Você excedeu o limite permitido que é de 80KM/hr")
    print(f"O valor da multa será R${(velocidade - 80)* 7:.2f}")

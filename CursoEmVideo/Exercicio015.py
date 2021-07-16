''' 15 Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
  Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''

quantidade_de_km = float(input("Digite a quantidade de km percorridos: "))
quantidade_de_dias = int(input("Digite a quantidade de dias pelos quais ele foi alugado: "))

print(f"Você deverá pagar R$ {quantidade_de_km*0.15 + quantidade_de_dias*60}")
  

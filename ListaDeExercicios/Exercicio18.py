"""Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)."""


Download = float(input("Digite o tamanho do arquivo em MB:"));
Velocidade = float(input("Digite a velocidade de um link de Internet em Mbps: "));

Convertido = Velocidade /8;
Minuto = Convertido * 60;
Tempo = Download / Minuto

print("O download vai demorar {} minutos".format(Tempo));


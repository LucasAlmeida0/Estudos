''' O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. 
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

import random

Primeiro_aluno = str(input("Digite o nome do primeiro aluno: "))
Segundo_aluno = str(input("Digite o nome do segundo aluno: "))
Terceiro_aluno = str(input("Digite o nome do terceiro aluno: "))
Quarto_aluno = str(input("Digite o nome do quarto aluno: "))
lista = [Primeiro_aluno, Segundo_aluno, Terceiro_aluno, Quarto_aluno]
random.shuffle(lista)
print(f"A ordem dos alunos será: {lista}")
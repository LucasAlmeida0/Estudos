'''19 Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
 Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''

import random

Primeiro_aluno = str(input("Digite o nome do primeiro aluno: "))
Segundo_aluno = str(input("Digite o nome do segundo aluno: "))
Terceiro_aluno = str(input("Digite o nome do terceiro aluno: "))
Quarto_aluno = str(input("Digite o nome do quarto aluno: "))

print(f"O aluno escolhido foi {random.choice([Primeiro_aluno, Segundo_aluno, Terceiro_aluno, Quarto_aluno])}")


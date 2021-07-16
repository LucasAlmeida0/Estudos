dados = list()
pessoa = list()

# [PESSOA] [NOME/NOTAS] [NOTA1/NOTA2]
while True:
    pessoa.append(str(input('Nome: ')))
    notas = [int(input('Nota 1: ')),
            int(input('Nota 2: '))] 
    pessoa.append(notas[:])
    dados.append(pessoa[:])
    notas.clear()
    pessoa.clear()
    continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if continuar in 'N': break
print(dados)
print(pessoa)
print('-='*50)
print('N°     Nome              Média')
print('-'*30)
for contador_dados in range(0,len(dados)):
    print(f'{contador_dados}', end='    ')
    print(f'{dados[contador_dados][0]:<5}', end='')
    print(f'{(dados[contador_dados][1][0] +dados[contador_dados][1][1])/2:>30}')


while True:
    print('-'*30)
    aluno = int(input('Mostrar nota de qual aluno? [999 interrompe]'))
    if aluno == 999: break 
    print(f'Notas de {dados[aluno][0]} são {dados[aluno][1]}')

    
 # Nota:{(dados[contador_pessoa][1][0] + dados[contador_pessoa][1][1])/2}
 # Nome: {dados[contador_pessoa][0]}
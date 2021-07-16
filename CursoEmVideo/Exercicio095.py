# Declaração

lista_de_jogadores = list()



# Entrada
while True:
    gols = list()
    jogador = dict()
    jogador['nome'] = str(input('Nome: '))
    partidas = int(input('Partidas: '))
    for c in range(1, partidas+ 1):
        gols.append(int(input(f'Quantos gols foram feitos na {c}ª partida ')))
# Processamento
    jogador['gols'] = gols.copy()
    jogador['total'] = sum(gols)
    lista_de_jogadores.append(jogador.copy())
    del jogador, gols
    continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if continuar not in 'NS':
        while True:
            print('ERRO! Digite uma reposta valida!')
            continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
            if continuar in 'NS': break
    if continuar in 'N': break
    print('-'*30)

print('-'*30)

# Saida
for c in range(0,len(lista_de_jogadores)):
    print(f"cod :{c}  nome:{lista_de_jogadores[c]['nome']}  total: {lista_de_jogadores[c]['total']}  gols: {lista_de_jogadores[c]['gols']}")

while True:
    existe = 0
    mostrar = int(input('Mostrar qual jogador? [-1 para parar]'))
    if mostrar == -1: break
    elif mostrar <= len(lista_de_jogadores)-1:
        print('-'*30)
        print(f"LEVANTAMENTO DO JOGADOR {lista_de_jogadores[mostrar]['nome']}")
        for p in range(1,len(lista_de_jogadores[mostrar]['gols'])+1):
            print(f"No jogo {p} fez {lista_de_jogadores[mostrar]['gols'][p-1]} gols")
    else:
        print(f'ERRO! O número de jogador {mostrar} não existe! Tente Novamente!')
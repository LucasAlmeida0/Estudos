def voto(nascimento):
    from datetime import date
    atual = date.today().year
    idade =  atual - nascimento 
    if idade < 16: return f'Com {idade} anos: Voto Negado'
    elif idade < 18 or idade >= 65: return f'Com {idade} anos: Voto Opcional'
    else: return f'Com {idade} anos: Voto Obrigatório'


nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))
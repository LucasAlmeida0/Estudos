def notas(*notas, sit = False):
    '''
    -> Analisa a nota de alunos e sua situação
    :param notas: Uma ou mais notas dos alunos (aceita varias)
    :param sit: Mostrar ou não a situação do aluno
    :return: Dicionario com todas informações solicitadas
    '''
    turma = dict()
    soma = 0

    turma['tamanho'] = len(notas)
    turma['maior'] = max(notas)
    turma['menor'] = min(notas)
    turma['media'] =  sum(notas)/len(notas)
    if sit:
        if sum(notas)/len(notas) < 5:
            turma['situacao'] = 'RUIM'
        elif sum(notas)/len(notas) < 7:
            turma['situacao'] ='RAZOÁVEL'
        else:
            turma['situacao'] ='BOA'
    return turma

resp = notas(1,2,3,4,5,6,7,8,1, sit=True)
print(resp)
help(notas)
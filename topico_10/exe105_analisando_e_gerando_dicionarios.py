def notas(*n, sit=False):
    '''
    Funções para notas dos alunos.
    :param n: notas dos alunos
    :param sit: valor opcionnal se deve ou não adicionar a situação
    :return: dicionário com várias informações dos alunos
    '''
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'Boa'
        elif r['media'] >= 5:
            r['situação'] = 'Razoável'
        else:
            r['situação'] = 'Ruim'
    return r

resp = notas(5.5, 2.5, 8.5, sit=True)
print(resp)
help(notas)
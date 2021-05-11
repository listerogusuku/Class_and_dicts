'''
def contabiliza_combustivel(dicionario_de_vendas):
    dic = {}
    for diaria in dicionario_de_vendas:
        if dicionario_de_vendas[diaria]['tipo'] in dic:
            dic[dicionario_de_vendas[diaria]['tipo']]['total litros'] += dicionario_de_vendas[diaria]['litros']
            dic[dicionario_de_vendas[diaria]['tipo']]['custo por litro'] += dicionario_de_vendas[diaria]['custo']
            dic[dicionario_de_vendas[diaria]['tipo']]['custo por litro'] = dic[dicionario_de_vendas[diaria]['tipo']]['custo por litro']/dic[dicionario_de_vendas[diaria]['tipo']]['total litros']
        else:
            dic[dicionario_de_vendas[diaria]['tipo']] = {'total litros': dicionario_de_vendas[diaria]['litros'], 'custo por litro': dicionario_de_vendas[diaria]['custo']}

    return dic
'''


def contabiliza_combustivel(dicionario_de_vendas):
    dic={}
    for diaria in dicionario_de_vendas:
        if dicionario_de_vendas[diaria]['tipo'] in dic:
            dic[dicionario_de_vendas[diaria]['tipo']]['total litros'] += dicionario_de_vendas[diaria]['litros']
            dic[dicionario_de_vendas[diaria]['tipo']]['custo por litro'] += dicionario_de_vendas[diaria]['custo']
            dic[dicionario_de_vendas[diaria]['tipo']]['custo por litro'] = (dic[dicionario_de_vendas[diaria]['tipo']]['custo por litro']/dic[dicionario_de_vendas[diaria]['tipo']]['total litros'])
        else:
            dic[dicionario_de_vendas[diaria]['tipo']]={'total litros':dicionario_de_vendas[diaria]['litros'],'custo por litro':dicionario_de_vendas[diaria]['custo']}

    return dic





entrada = {
    'dia 3': {
        'tipo': 'Ar',
        'litros': 100,
        'custo': 20.0
    },
    'dia 5': {
        'tipo': 'Gasolina',
        'litros': 25,
        'custo': 175.0
    },
    'dia 20': {
        'tipo': 'Ar',
        'litros': 50,
        'custo': 10.0
    }
}


'''
{
    'dia 1': {
        'tipo': 'Etanol',
        'litros': 20,
        'custo': 50.0
    },
    'dia 4': {
        'tipo': 'Gasolina',
        'litros': 25,
        'custo': 150.5
    },
    'dia 10': {
        'tipo': 'Gasolina',
        'litros': 15,
        'custo': 49.5
    },
    'dia 14': {
        'tipo': 'Etanol',
        'litros': 30,
        'custo': 70.0
    }
}
'''
print(contabiliza_combustivel(entrada))
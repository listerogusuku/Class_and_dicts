def funcao(dic):
    dic1={}
    for dia in dic:
        if dic[dia]['tipo'] in dic1:
            dic1[dic[dia]['tipo']]['total litros']+=dic[dia]['litros']
            dic1[dic[dia]['tipo']]['custo por litro']+=dic[dia]['custo']/dic[dia]['litros']
        else:
            dic1[dic[dia]['tipo']]={'total litros':dic[dia]['litros'],'custo por litro':dic[dia]['custo']/dic[dia]['litros']}

    return dic1


contabiliza_combustivel = {'dia 1': {
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
    'tipo': 'Etanol',
    'litros': 15,
    'custo': 49.5
    },
    'dia 14': {
    'tipo': 'Etanol',
    'litros': 30,
    'custo': 70.0
    }
}

print(funcao(contabiliza_combustivel))
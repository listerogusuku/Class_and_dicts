# dados = list()
# dados.append('Pedro')
# dados.append(25)
# print(dados[0])
# print(dados[1])

'''
dados2 = dict()
dados2 = {'nome':'Lister', 'idade': 20}
dados2['sexo'] = 'M'
print(dados2['sexo'])
del dados2['idade']
'''

'''
filmes = {

    'título': 'Star Wars',
    'ano': '1977',
    'director': 'George Lucas',

}

print(filmes.values())
print(filmes.keys())
print(filmes.items())

print('\n')

for k, v in filmes.items():
    print(f'O {k} é {v}')

print('\n')
'''


'''
pessoas = {

    'nome':'Gustavo', 'sexo':'M', 'idade':22

}

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

print()

print(pessoas.keys())
print()

print(pessoas.values())

print(pessoas.items())

print()

pessoas['peso'] = 98.5
for k,v in pessoas.items(): #Nas tuplas e listas eu preciso usar o enumerate, já nos dicionários eu posso usar apenas o items
    print(f'{k} = {v}')
'''


'''
brasil = []

estado1 = {
    'UF': 'Rio de Janeiro', 'sigla': 'RJ'
}

estado2 = {
    'UF':'São Paulo', 'sigla': 'SP'
}

brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil)

print()

print(brasil[0]['UF'])
'''



'''
estado = dict()
brasil = list()

for i in range(0,3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())

print(brasil)

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
    # print(e)


'''

'''
aluno_1 = {
    'Nome':'Lister',
    'Nota': 10,
    'Média': 8.5,
    'Situação': 'Aprovado'
}

aluno_2 = {
    'Nome':'Ykaro',
    'Nota': 9,
    'Média': 9.3,
    'Situação': 'Aprovado'
}

aluno_3 = {
    'Nome': 'Adney',
    'Nota': 10,
    'Média': 9.8,
    'Situação': 'Aprovado',
}

nomes = []

nomes.append(aluno_1)
nomes.append(aluno_2)
nomes.append(aluno_3)

print(nomes)

nome = str(input('Digite o nome do aluno desejado: '))

print(f'O aluno {nomes[nome]} obteve média {nomes[nome]["Média"]}')
'''



'''
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

# print(aluno)


for k, v in aluno.items():
    print(f'{k} é igual a {v}')
'''


'''
contato = { 'Nome': 'Lister', 'Telefone': 65987561230 , 'Celular': 91114562341, 'E-mail': 'ogusuku@ogusuku.com'}

contato['Localidade'] = 'São Paulo/SP'

print(contato['Nome'])
print(contato['Localidade'])

print()

print(contato)

print()

dictio = {'Nome': ['Lister Ogusuku Ribeiro', 21]}

print(f'Seu nome é: {dictio["Nome"][0]} e sua idade {dictio["Nome"][1]} anos')

'''

'''
contato = { 'Nome': 'Lister', 'Telefone': 65987561230 , 'Celular': 91114562341, 'E-mail': 'ogusuku@ogusuku.com'}

for lister, rodrigo in contato.items():
    print(f'{lister} = {rodrigo}')

oi = 'Endereço' in contato
print(oi)
'''

'''

contato = { 'Nome': 'Lister', 'Telefone': 65987561230, 'E-mail': 'ogusuku@ogusuku.com'}

def get(dic, key, valor=None):
    if key in dic:
        return dic[key]
    else:
        return valor

print(get(contato,'Nome'))
print()
print(get(contato, 'Celular', 8888888))
'''

contato = { 'Nome': 'Lister', 'Telefone': 65987561230, 'E-mail': 'ogusuku@ogusuku.com'}

def items(dic):
    lista = []
    for key in dic:
        lista.append((key, dic[key]))

    print(lista)

print(items(contato))

contato2 = contato.copy()
contato2['11'] = 11
print(contato2)
print(contato)

contato2.pop('11')
print()
print(contato2)

print()

print(contato2.setdefault('Smartphone'))

print(contato2)

contato2.pop('Smartphone')
print()
print(contato2)

contato2.setdefault('Smartphone', 17997756342)
print()
print(contato2)
print()

def muda(dic):
    dic.setdefault('1234', 'Dart Vader')

print(muda(contato))
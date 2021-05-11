string = 'piu-piu'

x = string.find('-')

print(x)

lista1 = string[0:x]
print(lista1)

lista2 = string[x+1:]
print(lista2)


if lista1 == lista2:
    print('True')
else:
    print('False')

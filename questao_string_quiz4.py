def palavras_sao_iguais(palavra):
    localiza_hifen = palavra.find('-')

    primeira_fatia = palavra[0:localiza_hifen]
    segunda_fatia = palavra[localiza_hifen+1:]

    if primeira_fatia == segunda_fatia:
        return True
    else:
        return False


print(palavras_sao_iguais('zigue-zague'))
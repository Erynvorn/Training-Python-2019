#change Polish character to roman

def correct_polish_letters(st): 
    cont = ''
    translation = {'ą':'a','ć': 'c','ę':'e','ł':'l','ń':'n', 'ó': 'o', 'ś' :'s','ź':'z','ż':'z' }
    for i in st:
        cont += translation.get(i, i)
    return cont


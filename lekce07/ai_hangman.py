from random import choice

def vyber_slovo():
    '''pocitac vybere slovo z pripraveneho seznamu'''
    seznam_slov = ['rajce', 'cibule', 'jablko']
    hadane_slovo = choice(seznam_slov)
    return hadane_slovo
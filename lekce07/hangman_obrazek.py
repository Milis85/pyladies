
def vypis_obrazek(pocet_pokusu):
    '''vykresli obrazek obesence podle poctu chybnych pokusu'''
    with open (str(pocet_pokusu) + '.txt', 'r', encoding = 'utf-8') as soubor:
        obsah = soubor.read()
        return obsah
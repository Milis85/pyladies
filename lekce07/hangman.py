from string import ascii_lowercase
from ai_hangman import vyber_slovo
from hangman_obrazek import vypis_obrazek

'''sibenice obrazky se nacitaji z jednotlivych .txt souboru'''

def zamen(stav_pole, pozice, pismeno):
    '''zapise do pole pismeno - pokud se uzivatel trefi'''
    return stav_pole[:pozice] + pismeno + stav_pole[pozice + 1:]

def zadej_pismeno():
    '''Nacita pismeno od uzivatele tak dlouho, dokud nezada pismeno'''
    abeceda = ascii_lowercase
    while True:
        pismeno = input('Zadej pismeno: ')
        if len(pismeno) == 1 and pismeno in abeceda:
            return pismeno
        else:
            print('Je potreba zadat pismeno!')

def hra():
    '''samotna hra sibenice'''
    slovo = vyber_slovo()
    stav_pole = len(slovo) * '-' #vytvori hraci pole
    print(stav_pole)
    pocet_pokusu = 0
    while '-' in stav_pole:
        pismeno = zadej_pismeno()
        if pismeno in slovo:
            pozice = slovo.index(pismeno)
            stav_pole = zamen(stav_pole, pozice, pismeno)
            print(stav_pole)
        else:
            pocet_pokusu += 1
            print(vypis_obrazek(pocet_pokusu))
            print('Chybny tah')
            print(stav_pole)
            if pocet_pokusu == 10:
                print(f'Prohravas, hadane slovo bylo {slovo}')
                break    
    else:
        print(f'Velmi dobre, gratuluji! Hadane slovo bylo skutecne {slovo}.')

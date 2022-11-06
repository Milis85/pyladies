from random import randrange  #pro nahodny tah pocitace

def tah_pocitace(pole):
    '''Vrátí herní pole se zaznamenaným tahem počítače
1. Vyber číslo od 0 do 19.
2. Pokud je dané políčko volné, hrej na něj.
3. Pokud ne, opakuj od bodu 1.'''
 
    while True:
        cislo_policka = randrange(20)
        if pole[cislo_policka] == '-':
            return tah(pole, cislo_policka, 'o')

def tah(pole, cislo_policka, symbol):
    '''Napiš funkci tah, která dostane řetězec s herním polem, číslo políčka (0-19), a symbol (x nebo o) a vrátí
    herní pole (t.j. řetězec) s daným symbolem umístěným na danou pozici.'''
    return pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]   

        
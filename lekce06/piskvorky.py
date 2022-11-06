
def vyhodnot(pole):
    '''vyhodnoti stav v radku
    "x" – Vyhrál hráč s křížky (pole obsahuje xxx)
    "o" – Vyhrál hráč s kolečky (pole obsahuje ooo)
    "!" – Remíza (pole neobsahuje -, a nikdo nevyhrál)
    "-" – Ani jedna ze situací výše (t.j. hra ještě neskončila)'''

    if "xxx" in pole:
        return('x')
    elif 'ooo' in pole:
        return('o')
    elif '-' not in pole:
        return('!')
    else:
        return('-')

def tah(pole, cislo_policka, symbol):
    '''Napiš funkci tah, která dostane řetězec s herním polem, číslo políčka (0-19), a symbol (x nebo o) a vrátí
    herní pole (t.j. řetězec) s daným symbolem umístěným na danou pozici.'''
    return pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]
    

def tah_hrace(pole):
    '''zeptá se hráče, na kterou pozici chce hrát a vrátí herní pole se zaznamenaným tahem hráče.
    Funkce by měla odmítnout záporná nebo příliš velká čísla a tahy na obsazená políčka. Pokud uživatel
    zadá špatný vstup, funkce mu vynadá a zeptá se znova.'''
    while True:
        cislo_policka = int(input('Zadej cislo policka, ktery hrajes (rozmezi 0-19): '))
        if cislo_policka >= 0 and cislo_policka <= 19 and pole[cislo_policka] == '-':
            return tah(pole, cislo_policka, 'x')
            
        else:
            print('Zadal si spatne policko, bud si s cislem uplne vedle nebo je uz obsazene.')

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
        

def piskvorky1d():
    '''Napiš funkci piskvorky1d, která vytvoří řetězec s herním polem a střídavě volá funkce tah_hrace a
    tah_pocitace, dokud někdo nevyhraje nebo nedojde k remíze.'''
    pole = 20 * '-'
    while True:
        
        pole = tah_hrace(pole)
        print(pole)
        pole = tah_pocitace(pole)
        print(pole)
        vyhodnot(pole)
        if vyhodnot(pole) != '-':
            break
   
    print('Vyhral', vyhodnot(pole))


piskvorky1d()    
    


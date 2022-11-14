from ai import tah_pocitace

def vyhodnot(pole):
    if "xxx" in pole:
        return'x'
    elif 'ooo' in pole:
        return'o'
    elif '-' not in pole:
        return'!'
    else:
        return'-'

def tah(pole, cislo_policka, symbol):
    
    return pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]   

def tah_hrace(pole):
    while True:
        cislo_policka = input('Zadej cislo policka, ktery hrajes (rozmezi 0-19): ')
        if not cislo_policka.isdigit():
            print('Zadej cislo geeez!')
            continue
        
        cislo_policka = int(cislo_policka)    
        
        if cislo_policka in range(0, 20) and pole[cislo_policka] == '-':
            return tah(pole, cislo_policka, 'x')
            
        else:
            print('Zadal si spatne policko, bud si s cislem uplne vedle nebo je uz obsazene.')

def piskvorky1d():
    pole = 20 * '-'
    vitez = '-'
    while True:
        
        pole = tah_hrace(pole)
        print(pole)
        pole = tah_pocitace(pole)
        print(pole)
        vitez = vyhodnot(pole)
        if vitez != '-':
            break
   
    print('Vyhral', vitez)

   
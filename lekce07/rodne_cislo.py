rodne_cislo = input('zadej rodne cislo: ')
def nacti_cislo():
    try: 
        int(rodne_cislo)
    except ValueError:
        print('zadane cislo je ve spatnem formatu')
        exit()

   
''' Je ve správném formátu: 6 číslice, lomítko, 4 číslice? (vrací True nebo False'''
def format(cislo):       
    cislo_seznam = cislo.split('/', 1)
    try:
        return len(cislo_seznam[0]) == 6 and len(cislo_seznam[1]) == 4
    except IndexError:
        print('spatny format cisla')
        exit()

print(format(rodne_cislo))

'''Je dělitelné jedenácti? (vrací True nebo False)'''

def delitelnost(cislo):
    try:
        cislo_seznam = cislo.split('/', 1)
        cislo_bez_lomitka = int(''.join(cislo_seznam))  
    except ValueError: 
        print('Nebylo zadano spravne rodne cislo')
        if cislo_bez_lomitka % 11 == 0:
            print (True)

            
print(delitelnost(rodne_cislo))

'''Jaké datum narození je v čísle zakódováno? (vrací trojici čísel – den, měsíc, rok)'''

def datum(cislo):
    den = cislo[4:6]
    mesic = int(cislo[2:4])

    if mesic > 50:
        mesic_zena_muz = mesic - 50
        print(mesic_zena_muz)
    else:
        mesic_zena_muz = mesic

    rok = int(cislo[0:2])
    if rok > 84:
       rok_narozeni = '{}{}'.format(19, rok)
    else:
        rok_narozeni = '{}{}'.format(20, rok) 
    datum_narozeni = f'{den}.{mesic_zena_muz}.{rok_narozeni}'
    return datum_narozeni
print(datum(rodne_cislo))

'''Jaké pohlaví je v čísle zakódováno? (vrací 'muž' nebo 'žena')'''

def pohlavi(cislo):
    mesic = int(cislo[2:4])
    if mesic > 50:
        pohlavi = 'zena'
    else:
        pohlavi = 'muz'
    return pohlavi
print(pohlavi(rodne_cislo))

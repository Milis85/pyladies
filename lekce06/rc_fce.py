#Napiš tyto funkce. Každá z nich dostane jako argument řetězec s rodným číslem a nějak ho zanalyzuje:
#(a) Je ve správném formátu: 6 číslice, lomítko, 4 číslice? (vrací True nebo False
# (b) Je dělitelné jedenácti? (vrací True nebo False)
#(c) Jaké datum narození je v čísle zakódováno? (vrací trojici čísel – den, měsíc, rok)
#(d) Jaké pohlaví je v čísle zakódováno? (vrací 'muž' nebo 'žena')

#Pro účely úkolu stačí, když bude program umět zpracovat čísla vydávaná od roku 1985. Reálná rodná čísla můžou být složitější :)

#Napiš program který se uživatele zeptá na rodné číslo a vypíše výsledky.


while True:
    rodne_cislo = input('zadej rodne cislo: ')
    if rodne_cislo.count('/') == 1 and rodne_cislo.index('/') == 6 and len(rodne_cislo) == 11:
        break
    print('zadej rodne cislo ve formatu yymmddd/nnnn')

    
''' Je ve správném formátu: 6 číslice, lomítko, 4 číslice? (vrací True nebo False'''
def format(cislo):       
    cislo_seznam = cislo.split('/', 1)
   
    if len(cislo_seznam[0]) == 6 and len(cislo_seznam[1]) == 4:
        return True
    else:
        return False

print(format(rodne_cislo))

'''Je dělitelné jedenácti? (vrací True nebo False)'''

def delitelnost(cislo):
    cislo_seznam = cislo.split('/', 1)
    cislo_bez_lomitka = int(''.join(cislo_seznam))   
    if cislo_bez_lomitka % 11 == 0:
        return True
    else:
        return False
            
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
    datum_narozeni = (f'{den}.{mesic_zena_muz}.{rok_narozeni}')
    return datum_narozeni
print(datum(rodne_cislo))

#Jaké pohlaví je v čísle zakódováno? (vrací 'muž' nebo 'žena')

def pohlavi(cislo):
    mesic = int(cislo[2:4])
    if mesic > 50:
        pohlavi = 'zena'
    else:
        pohlavi = 'muz'
    return pohlavi
print(pohlavi(rodne_cislo))








#prepis Kamen, Nuzky, Papir pomoci and a or

from random import randrange

tah_pocitace = randrange(3)
tah_cloveka = input('Vybral sis kamen, nuzky nebo papir? ')

if tah_pocitace == 0:
    tah_pocitace = 'kamen'
    print('Pocitac si vybral kamen')
elif tah_pocitace == 1:
    tah_pocitace = 'nuzky'
    print('Pocitac si vybral nuzky')
else:
    tah_pocitace = 'papir'
    print('Pocitac si vybral papir')
    

if tah_cloveka == tah_pocitace:
    print('Plichta')
elif ((tah_cloveka == 'kamen') and (tah_pocitace == 'nuzky')) or ((tah_cloveka == 'nuzky') and (tah_pocitace == 'papir')) or ((tah_cloveka == 'papir') and (tah_pocitace == 'kamen')):
    print("Vyhral jsi!")
else:
    print('Prohral jsi!')

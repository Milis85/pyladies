from random import randrange
#vyber karet do hodnoty 21, zastavi se ve chvili, kdy bude odpoved na dalsi kartu ne
soucet = 0
while soucet < 21:
    print ('mas', soucet, 'bodu')
    odpoved = input('Otocit kartu? ')
    if odpoved == 'ano':
        karta = randrange(2, 11)
        print('Otocila jsi', karta)
        soucet = soucet + karta
    elif odpoved == 'ne':
        break
    else:
        print('Nerozumim" Odpovidej "ano" nebo "ne"')
#pokud soucet dosahne 21 vyhravam
#pokud presahne prohravam
if soucet == 21:
    print('Gratuluji! Vyhrala si!')
elif soucet > 21:
    print('Smula!', soucet, 'bodu je moc!')
else:
    print('Chybelo ti jen', 21- soucet, 'bodu!')

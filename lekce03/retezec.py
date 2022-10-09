#zadam slovo, vyberu pozici znaku, ktery menim a vypisu novy znak
retezec = input('Zadej retezec: ')
pozice = int(input('Kolikaty znak budeme nahrazovat? '))
znak = input('Novy znak?' )
#takhle bude vypadat nove slovo
print(retezec[:pozice] + znak + retezec[pozice + 1:])



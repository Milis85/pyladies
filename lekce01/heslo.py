
#napis program, ktery po zadani spravneho hesla vyzradi tajemstvi

heslo = input('Rekni heslo: ')
heslo_je_spravne = heslo == 'ponozka'

if heslo_je_spravne:
    print('Jezisek neexistuje!')
else:
    print('Smula, nic ti nepovim')
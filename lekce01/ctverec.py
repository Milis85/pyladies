

strana = float(input('Zadej cislo strany '))#v centimetrech

cislo_je_spravne = strana > 0

if cislo_je_spravne:
    print('Obvod ctverce se stranou', strana, 'cm je', 4 * strana, 'cm')
    print('Obsah ctvrece se stranou', strana, 'cm je', strana * strana, 'cm')
else:
    print('Strana musi byt kladna, jinak z toho nebude ctverec!')

print('Dekujeme za pouziti geometricke kalkulacky')

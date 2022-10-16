#zasifruje zadanou zpravu
#plaintext se vzpise jako mala pismena
plaintext = (input('Zadej zpravu: ')).lower()
ciphertext = ' '
#dokud uzivatel nezada sravny klic, sifrovani se neprovede
while True:
    key = int(input('Zadej klic: '))
    if key >= 0 and key <= 25:
        break
    print('Klic musi byt kladne cislo v rozmezi 0-25!')

print('OK, jdeme sifrovat.')
#kazde pismeno ze zpravy se prevede do ASCII tabulky, posunese se o pocet znaku 
# dle promenne 'key', cislo 97 znamena, ze se ma brat abeceda malych pismen v ASCII tabulce
# mezera nebude prevadena   
for pismeno in plaintext:
    if pismeno != ' ':
        nove_pismeno = chr((ord(pismeno) - 97 + key) % 26 + 97)
        ciphertext = ciphertext + nove_pismeno
    else:
        ciphertext += pismeno
print(f'Zasifrovany text je{ciphertext}')









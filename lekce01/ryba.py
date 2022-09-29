#program, ktery vypise ruzne nesmysly 

ryba = float(input('kolik kilo ta ryba vazi? '))

if ryba >= 50:
    print('Wau, to je poradny kousek')
elif ryba >= 10:
    print('Hm, asi budes sikovny rybar') 
elif ryba >= 5:
    print('Neni to nejs=horsi ulovek...')
elif ryba >= 1:
    print ('Tak to je takovy kaprik na Vanoce, co?')
elif ryba >=0.01:
    print('Vrat tu nebohou rybku do akvaria')
else:
    print('Nech ty ryby byt, ryba je kamos ne zradlo...')

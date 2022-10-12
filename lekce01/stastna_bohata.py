#prepis program "stastna bohata" se zanorenymi ify
#ktera verze ti prijde citelnejsi?
#tahle

stastna = input('Jsi stastna? ')
bohata = input('Jsi bohata? ')

if stastna == 'ano':
    if bohata == 'ano':
        print('Gratuluji!')
    else:
        print('Zkus min utracet!')
else:
    if bohata == 'ano':
        print('Vic se usmivej!')
    else:
        print('To je mi lito')
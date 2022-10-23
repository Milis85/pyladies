#vytvoř program, který zvířata seřadí podle abecedy, ale bude
#ignorovat první písmeno
#Postup:
#Vytvoř seznam dvojic (klíč, hodnota).
#Seřaď tento seznam dvojic – dvojice se řadí nejdřív podle prvního prvku, pak druhého atd.
#Nakonec vytvoř ze seznamu dvojic opět jen seznam hodnot

zvirata = ["andulka", "had", "pes", "kočka", "králík"]
druhe_pismeno = []
dvojice = []
seznam_hodnot = []

for zvire in zvirata:
    druhe_pismeno.append(zvire[1])
    dvojice.append((zvire[1], zvire))


druhe_pismeno.sort()
slovnik = dict(dvojice)  
  
for i in druhe_pismeno:
    if i in slovnik:
        seznam_hodnot.append(slovnik[i]) 

print(seznam_hodnot)


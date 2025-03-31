"""
Olvasd be az f1.txt adatait, majd oldd meg az alábbi feladatokat!

1. Hány versenyző szerepel a fájlban?
2. Melyik versenyző nyerte a legtöbb futamot?
3. Ki teljesített a legtöbb futamot?
4. Átlagosan hány futamot teljesítettek a versenyzők?"

A megoldott feladatokat a kiirt_adatok nevű mappába hozd létre statisztika.txt néven!
"""




adat = []

with open('beolvasando_adatok/f1.txt', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        nev, csapat, gyozelmek_szama, teljitesett_futamok_szama = sor.strip().split(';')
        adat.append([nev, csapat, int(gyozelmek_szama), int(teljitesett_futamok_szama)])

#for i in range(len(adat)):
#    print(adat[i])

max_verseny = 0
maxim_teljesitett = 0

for i in range(len(adat)):
    if adat[i][2] > max_verseny:
        max_verseny = adat[i][2]
    if adat[i][3] > maxim_teljesitett:
        maxim_teljesitett = adat[i][3]


# print(f"A beolvasott fájlban összesen {adat} versenyző szerepel.")
print(f"A legtöbb futamot nyert versenyző: {max_verseny} ")
print(f"A legtöbb futamot teljesített versenyző: {maxim_teljesitett}")
print(f"Az átlagos futamszám: ____")
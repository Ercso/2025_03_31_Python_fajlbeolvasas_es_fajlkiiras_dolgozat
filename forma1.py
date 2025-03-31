"""
Olvasd be az f1.txt adatait, majd oldd meg az alábbi feladatokat!

1. Hány versenyző szerepel a fájlban?
2. Melyik versenyző nyerte a legtöbb futamot?
3. Ki teljesített a legtöbb futamot?
4. Átlagosan hány futamot teljesítettek a versenyzők?"

A megoldott feladatokat a kiirt_adatok nevű mappába hozd létre statisztika.txt néven!
"""



forrasfajl = open('beolvasando_adatok/f1.txt', 'r', encoding='utf-8')

adat = []

with open('beolvasando_adatok/f1.txt', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        nev, csapat, gyozelmek_szama, teljitesett_futamok_szama = sor.strip().split(';')
        adat.append([nev, csapat, gyozelmek_szama, teljitesett_futamok_szama])

max_verseny = max(adat, key=lambda x: (x[2]))

maxim_teljesitett = max(adat, key=lambda x: (x[3]))

adat = 

print(f"A beolvasott fájlban összesen {adat} versenyző szerepel.")
print(f"A legtöbb futamot nyert versenyző: {max_verseny} ")
print(f"A legtöbb futamot teljesített versenyző: {maxim_teljesitett}")
print(f"Az átlagos futamszám: ____")
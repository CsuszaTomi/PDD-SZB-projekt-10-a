#tabla sablonja(remélem már jó)
teljes_tabla = """\
┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
│ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │
├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
│ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │
├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
│ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │
├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
│ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │
├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
│ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │
├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
│ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │
├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
│ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │
├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
│ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │
├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
│ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │
├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
│ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │
└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘"""

def töltés_tabla():
    tábla = []
    for sor in range(10):
        sor_mezők = []
        for oszlop in range(10):
            sor_mezők.append(" ")
        tábla.append(sor_mezők)
    return tábla

def rajzol_tábla(tábla):
    tábla_értékek = []
    for sor in tábla:
        for mező in sor:
            tábla_értékek.append(mező)  
    print(teljes_tabla.format(*tábla_értékek))
    
def jatekoslep(tábla, játékos):
    while True: 
        try:
            #bekeres
            print(f"{játékos} játékos következik!")
            sor_szám = int(input("Add meg a sor számát (0-9): "))
            oszlop_szám = int(input("Add meg az oszlop számát (0-9): "))
            #tablaba van?
            if sor_szám < 0 or sor_szám > 9 or oszlop_szám < 0 or oszlop_szám > 9:
                print("Hiba: A megadott pozíció kívül esik a táblán! Próbáld újra.")
                continue
            #üres?
            if tábla[sor_szám][oszlop_szám] != " ":
                print("Hiba: Ez a mező már foglalt! Próbáld újra.")
                continue
            tábla[sor_szám][oszlop_szám] = játékos
            break
        except ValueError:
            print("Hiba: Csak számokat adhatsz meg! Próbáld újra.")
            
#Ellenörzés
def ellenorzes(tábla, játékos):
    #sor ell
    for sor in tábla:
        if "".join(sor).find(játékos * 5) != -1:  #ha öt van egymas mellet
            return True
    # oszlop ell
    for oszlop_idx in range(10):
        oszlop = []
        for sor_idx in range(10):
            oszlop.append(tábla[sor_idx][oszlop_idx]) 
        if "".join(oszlop).find(játékos * 5) != -1:  # ha öt van egymas alatt
            return True
    # atlo(elvileg jó)
    for kezdo_sor in range(6):  
        for kezdo_oszlop in range(6):
            if all(tábla[kezdo_sor + i][kezdo_oszlop + i] == játékos for i in range(5)):
                return True
            if all(tábla[kezdo_sor + i][kezdo_oszlop + 4 - i] == játékos for i in range(5)):
                return True
    return False

def amoba():
    tábla = töltés_tabla()
    aktuális_játékos = "X"
    lépés_számláló = 0
    while lépés_számláló < 100:  #max 100 lepes
        rajzol_tábla(tábla)

        #lepes
        jatekoslep(tábla, aktuális_játékos)

        if ellenorzes(tábla, aktuális_játékos):
            rajzol_tábla(tábla)
            print(f"Gratulálunk, {aktuális_játékos} játékos nyert!")
            return

        #valtas
        if aktuális_játékos == "X":
            aktuális_játékos = "O"
        elif aktuális_játékos == "O":
            aktuális_játékos = "X"

        lépés_számláló += 1

    # ha betelt a tabla
    rajzol_tábla(tábla)
    print("Döntetlen! A tábla megtelt.")
    
#indito
amoba()

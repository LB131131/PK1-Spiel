import csv
import os
import time
import msvcrt
from farben import Farbe

skript_pfad = os.path.dirname(os.path.abspath(__file__))
DATEINAME = os.path.join(skript_pfad, 'highscores.csv') 

#code von Gemini 3 Pro

def highscores_verwalten(level,startzeit):
    str_zeit, dauer_sekunden=_zeitmessung(startzeit)
    name=_namensabfrage()
    _csv_save(level,dauer_sekunden,name)
    _zeige_top_liste()

def _zeitmessung(startzeit):
    endzeit=time.time()
    dauer_sekunden=int(endzeit-startzeit)
    minuten=dauer_sekunden//60
    sekunden=dauer_sekunden%60
    str_zeit=f'{minuten:02d}:{sekunden:02d}'
    return str_zeit, dauer_sekunden

def _namensabfrage():
    while msvcrt.kbhit():
        msvcrt.getch()
    
    name = input("Dein Name: ").strip()
    if not name: 
        name = "Unbekannt"
    return name
#code von Gemini 3 Pro

def _csv_save(erreichtes_level,dauer_sekunden,name):
    datei_existiert = os.path.isfile(DATEINAME)
    
    with open(DATEINAME, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # Wenn Datei neu ist -> Kopfzeile schreiben
        if not datei_existiert:
            writer.writerow(["Level", "Sekunden", "Name", "Datum"])
        
        # Daten schreiben
        datum_heute = time.strftime("%d.%m.%Y")
        writer.writerow([erreichtes_level, dauer_sekunden, name, datum_heute])
#code von Gemini 3 Pro

def _zeige_top_liste():
    scores = []
    
    if os.path.exists(DATEINAME):
        with open(DATEINAME, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None) 
            
            for zeile in reader:
                if zeile:
                    try:
                        lvl = int(zeile[0])
                        sek = int(zeile[1])
                        name = zeile[2]
                        scores.append((lvl, sek, name))
                    except:
                        continue 

    scores.sort(key=lambda x: (-x[0], x[1]))

    _header_anzeigen()

    for i, (lvl, sek, name) in enumerate(scores[:5]):
        m = sek // 60
        s = sek % 60
        zeit_fmt = f"{m:02d}:{s:02d}"
        print(f"{i+1:<6} | {lvl:<6} | {zeit_fmt:<8} | {name}")
    
    print("-" * 45)
    print("\nDrücke eine TASTE zum Beenden...")
    while True:
        if msvcrt.kbhit():
            msvcrt.getch()
            return
#code von Gemini 3 Pro
        
def _header_anzeigen():
    os.system('cls')
    print(Farbe.BLAU + "==========================================")
    print("           🏆 HALL OF FAME 🏆             ")
    print("==========================================" + Farbe.RESET)
    print(f"{'RANG':<6} | {'LVL':<6} | {'ZEIT':<8} | {'NAME'}")
    print("-" * 45)
#code von Gemini 3 Pro
import msvcrt
import time
import os
from farben import Farbe
def cheat_menue(spieler):
    while True:
        # Bildschirm einmal löschen
        os.system('cls')
        
        print(Farbe.GELB + "==========================================")
        print("      🛠️  CUSTOM DIFFICULTY MENÜ  🛠️      ")
        print("==========================================" + Farbe.RESET)
        
        # Aktuelle Werte anzeigen (formatiert gegen Anzeigefehler)
        print(f"Aktuelle Werte:")
        print(f"❤️  HP:       {spieler.getHP():<10}")
        print(f"🔋 Batterie: {spieler.getBatterie():<10}")
        print(f"⚔️  Schaden:  {spieler.schaden:<10}")
        
        print("-" * 42)
        print("[1] HP setzen (God Mode möglich)")
        print("[2] Batterie setzen (Unendlich möglich)")
        print("[3] Schaden setzen")
        print("[x] Zurück zum Spiel")
        print("-" * 42)
        print("Drücke eine Taste...")
        
        # Warten auf Taste (Verhindert Flackern)
        taste = msvcrt.getch().lower()
            
        if taste == b'1':
            wert = _eingabe_holen("Neue HP eingeben: ")
            if wert is not None:
                # TRICK: Wir greifen direkt auf die private Variable zu (_Klasse__variable)
                # Das umgeht die "Maximal 100"-Sperre aus setHP()
                spieler._Spieler__hp = wert
                _bestätigung(f"HP auf {wert} gesetzt!")
            
        elif taste == b'2':
            wert = _eingabe_holen("Neue Batterie eingeben: ")
            if wert is not None:
                # Auch hier: Sperre umgehen für unendlich Energie
                spieler._Spieler__batterie = wert
                _bestätigung(f"Batterie auf {wert} gesetzt!")
            
        elif taste == b'3':
            wert = _eingabe_holen("Neuen Schaden eingeben: ")
            if wert is not None:
                spieler.schaden = wert
                _bestätigung(f"Schaden auf {wert} gesetzt!")
            
        elif taste == b'x':
            os.system('cls')
            break
        
        # Kein sleep nötig, da getch() gewartet hat
#code von Gemini 3 Pro

def _eingabe_holen(nachricht):
    """Hilfsfunktion, um eine Zahl vom Benutzer abzufragen."""
    print("\n" + Farbe.BLAU + nachricht + Farbe.RESET, end="")
    
    try:
        eingabe = input() 
        zahl = int(eingabe)
        return zahl
    except ValueError:
        print(Farbe.ROT + "Das war keine gültige Zahl!" + Farbe.RESET)
        time.sleep(1)
        return None
#code von Gemini 3 Pro

def _bestätigung(text):
    print(Farbe.GRUEN + ">> " + text + " <<" + Farbe.RESET)
    time.sleep(1)
#code von Gemini 3 Pro
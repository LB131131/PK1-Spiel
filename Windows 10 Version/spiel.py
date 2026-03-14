import time
import os
import sys 
from farben import Farbe
from teilfunktionen import setup_spiel, map_zeichnen, inputs_holen, update_fahne, start_screen, verarbeite_zug
from scoreboard import highscores_verwalten
from cheats import cheat_menue
from savegame import spiel_speichern, spiel_laden

os.system("")

if __name__ == '__main__':
    
    start_screen()
    start_zeitpunkt=time.time()
    
    # --- STARTWERTE ---
    aktuelles_level = 1       
    mein_spieler = None       
    
    # KORREKTUR: Wir nutzen eine Variable, um zu wissen, wann wir bauen müssen
    neues_level_generieren = True

    # --- ÄUSSERE SCHLEIFE ---
    while True: 
        
        # Nur neues Level generieren, wenn wir nicht gerade geladen haben
        if neues_level_generieren:
            mein_spieler, map, gegner_liste, item_liste, ziel_coords = setup_spiel(aktuelles_level, mein_spieler)
            neues_level_generieren = False # Erledigt, Karte ist da
        
        level_geschafft = False 
        
        # --- INNERE SCHLEIFE ---
        while not level_geschafft:
            
            # 1. Zeichnen
            tor_offen = update_fahne(map, gegner_liste, ziel_coords)
            map_zeichnen(mein_spieler, map, gegner_liste, item_liste)
            
            # 2. Infos
            if tor_offen: 
                print(Farbe.GRUEN + f">>> WEG FREI! LEVEL {aktuelles_level} ABSCHLIESSEN! <<<" + Farbe.RESET)
            
            print(Farbe.GRAU + "[K] Speichern | [L] Laden | [B] Beenden" + Farbe.RESET)

            # 3. Input
            dx, dy, aktion = inputs_holen(mein_spieler)
            
            # --- AKTIONEN VERARBEITEN ---
            if aktion == 'quit': 
                sys.exit() 
            
            elif aktion == 'cheat':
                cheat_menue(mein_spieler)

            elif aktion == 'save':
                erfolg = spiel_speichern(mein_spieler, map, gegner_liste, item_liste, ziel_coords, aktuelles_level)
                if erfolg:
                    print(Farbe.GRUEN + ">> SPIEL GESPEICHERT! <<" + Farbe.RESET)
                    time.sleep(1)

            elif aktion == 'load':
                daten = spiel_laden()
                if daten:
                    try:
                        mein_spieler = daten["spieler"]
                        map = daten["map"]
                        gegner_liste = daten["gegner"]
                        item_liste = daten["items"]
                        ziel_coords = daten["koordinaten"] 
                        aktuelles_level = daten["level"]
                        
                        # WICHTIG: Wenn wir laden, wollen wir KEIN neues Level generieren
                        neues_level_generieren = False
                        
                        print(Farbe.BLAU + ">> SPIELSTAND GELADEN! <<" + Farbe.RESET)
                        time.sleep(1)
                    except KeyError:
                        print(Farbe.ROT + ">> FEHLER: Spielstand beschädigt oder veraltet! <<" + Farbe.RESET)
                        time.sleep(2)
                else:
                    print(Farbe.ROT + ">> KEIN SAVEGAME GEFUNDEN! <<" + Farbe.RESET)
                    time.sleep(1)

            # 4. Zug verarbeiten (nur wenn Bewegung da ist)
            if dx != 0 or dy != 0:
                status = verarbeite_zug(mein_spieler, map, gegner_liste, item_liste, dx, dy)
                
                if status == 'won':
                    print(Farbe.GRUEN + f"LEVEL {aktuelles_level} ABGESCHLOSSEN!" + Farbe.RESET)
                    time.sleep(2)
                    
                    aktuelles_level += 1      
                    level_geschafft = True
                    # WICHTIG: Jetzt sagen wir dem Spiel, dass es das nächste Level bauen soll
                    neues_level_generieren = True
    
                elif status == 'lost':
                    print(Farbe.ROT + "*** GAME OVER ***" + Farbe.RESET)
                    print(f"Du hast es bis Level {aktuelles_level} geschafft.")
                    time.sleep(2)
                    
                    # --- HIER WURDE DAS SCOREBOARD WIEDER EINGEFÜGT ---
                    highscores_verwalten(aktuelles_level, start_zeitpunkt)
                    
                    sys.exit() 

            time.sleep(0.05)
#code von Gemini 3 Pro
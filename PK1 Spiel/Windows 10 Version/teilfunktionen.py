import os
import time
import random
from konstanten import *
from map import *
from spieler import *
from gegner import *
from items import Heilung,Batterie,Schwert,Waffe,Laserschwert,Dolch
from farben import Farbe
import msvcrt
from cheats import cheat_menue

def berechne_kamera_offset(spieler, map, sicht_x, sicht_y):
    """Berechnet die obere linke Ecke des Kamera-Ausschnitts."""
    start_x = spieler.x - (sicht_x // 2)
    start_y = spieler.y - (sicht_y // 2)

    # Ränder prüfen (darf nicht kleiner 0 oder größer als Map sein)
    if start_x < 0: start_x = 0
    if start_y < 0: start_y = 0
    if start_x > map.breite - sicht_x: start_x = map.breite - sicht_x
    if start_y > map.höhe - sicht_y:   start_y = map.höhe - sicht_y
    
    return start_x, start_y
#code von Gemini 3 Pro

def hud_ausgeben(spieler, map, gegner_liste, item_liste, sicht_breite):
    waffen_symbol=FAUST
    if spieler.waffe:
        waffen_symbol=spieler.waffe.symbol

    print(f'HP:{spieler.getHP()} | Batterie:{spieler.getBatterie()} | Waffe: {waffen_symbol} | Schaden: {spieler.schaden}  ')
    #leerzeichen müssen dableiben weil sonst im hud 11 statt 1 schaden steht, wenn batterie oder hp nicht mehr dreistellig sind
    print(f'Level:{map.getLevel()} | Gegner verbleibend: {len(gegner_liste)} | Items verbleibend: {len(item_liste)}')

    print(('_' * sicht_breite) + "\033[K")
#code von Gemini 3 Pro

def get_aktuellen_radius(spieler):
    if spieler.getBatterie()<=0:
        return LICHT_RADIUS//2
    else:
        return LICHT_RADIUS
    
def bestimme_tile_symbol(x, y, spieler, map, radius_sq):
    """Entscheidet für EIN Feld, welches Symbol gezeichnet wird."""
    # Abstand berechnen
    dx = x - spieler.x
    dy = y - spieler.y
    abstand_sq = (dx * dx) + (dy * dy)

    # Ist das Feld im Lichtkegel?
    if abstand_sq <= radius_sq:
        if x == spieler.x and y == spieler.y:
            return SPIELER
        else:
            return map.grid[y][x]
    else:
        return DUNKELHEIT
#code von Gemini 3 Pro

def map_zeichnen(spieler, map, gegner_liste, item_liste):
    print("\033[H", end="")
    sicht_x = 60
    sicht_y = 24

    start_x, start_y = berechne_kamera_offset(spieler, map, sicht_x, sicht_y)
    hud_ausgeben(spieler, map, gegner_liste, item_liste, sicht_x)

    radius = get_aktuellen_radius(spieler)
    radius_sq = radius * radius

    for y in range(start_y, start_y + sicht_y):
        zeile = ''
        for x in range(start_x, start_x + sicht_x):
            zeile += bestimme_tile_symbol(x, y, spieler, map, radius_sq)
        print(zeile)
#code von Gemini 3 Pro

def setup_spiel(level_nummer=1, vorheriger_spieler=None):
    map=Map(MAP_BREITE,MAP_HÖHE, level_nummer)

    spieler=None
    if vorheriger_spieler is None:
        spieler=Spieler(MAP_BREITE//2,MAP_HÖHE//2)
    else:
        spieler=vorheriger_spieler
        spieler.x=MAP_BREITE//2
        spieler.y=MAP_HÖHE//2

    while map.ist_blockiert(spieler.x,spieler.y):
        spieler.x +=1

    if map.grid[spieler.y][spieler.x]==LAVA:
        map.grid[spieler.y][spieler.x]=BODEN

    if spieler.x>=map.breite-1:
        spieler.x=1
        spieler.y+=1

    g_liste=gegner_spawnen(map,spieler,4+level_nummer)
    i_liste=items_spawnen(map,spieler,2+level_nummer)

    while True:
        ziel_x=random.randint(1,map.breite-2)
        ziel_y=random.randint(1,map.höhe-2)
        if map.grid[ziel_y][ziel_x]==BODEN and (ziel_x!=spieler.x or ziel_y!=spieler.y):
            map.grid[ziel_y][ziel_x]=ZIEL_ROT
            ziel_koordinaten=(ziel_x, ziel_y)
            break
    
    return spieler,map,g_liste,i_liste,ziel_koordinaten

def gegner_spawnen(map, spieler, anzahl):
    liste = []
    typen = [Zombie, Geist, Skelett, Golem] 
    
    while len(liste) < anzahl:
        gx, gy = random.randint(1, map.breite-2), random.randint(1, map.höhe-2)

        if not map.ist_blockiert(gx, gy) and (gx != spieler.x or gy != spieler.y):
            # GEÄNDERT: Gegner nicht in Lava spawnen lassen
            if map.grid[gy][gx] == BODEN:  
                MonsterKlasse = random.choice(typen)
                monster = MonsterKlasse(gx, gy)
                liste.append(monster)
                map.grid[gy][gx] = monster.symbol
                
    return liste
#code von Gemini 3 Pro

def items_spawnen(map, spieler, anzahl):
    liste = []
    typen = [Heilung, Batterie, Heilung, Schwert, Dolch, Laserschwert] 

    while len(liste) < anzahl:
        ix, iy = random.randint(1, map.breite-2), random.randint(1, map.höhe-2)
        
        if not map.ist_blockiert(ix, iy) and (ix != spieler.x or iy != spieler.y):
            # GEÄNDERT: Items nicht in Lava spawnen lassen
            if map.grid[iy][ix] == BODEN: 

                if len(liste) < map.getLevel():
                    ItemKlasse = Heilung
                else:
                    ItemKlasse = random.choice(typen)

                item = ItemKlasse(ix, iy)
                liste.append(item)
                map.grid[iy][ix] = item.symbol
                
    return liste
#code von Gemini 3 Pro

def kampf_abwickeln(spieler, gegner, gegner_liste, map_obj):
    if isinstance(spieler.waffe, Laserschwert):
        kosten=5
        if spieler.getBatterie()>= kosten:
            spieler.setBatterie(spieler.getBatterie()-kosten)
            schaden=spieler.schaden
        else:
            schaden=0
    elif isinstance(spieler.waffe,Dolch):
        schaden=spieler.schaden
        spieler.waffe.treffer+=1
        if spieler.waffe.treffer%2==0:
            heilung=1
            spieler.setHP(spieler.getHP()+heilung)
    else:
        schaden=spieler.schaden

    gegner.schaden_nehmen(schaden)
    
    if gegner.hp <= 0:
        gegner_liste.remove(gegner)
        map_obj.grid[gegner.y][gegner.x] = BODEN
        return False
    
    if isinstance(gegner,Golem):
        pass
    else:
        schaden=gegner.stärke
        spieler.setHP(spieler.getHP()-schaden)
    
    if spieler.getHP() <= 0:
        return True
    else:
        return False

def item_einsammeln(spieler,item_liste,map):
    gefunden=None
    for i in item_liste:
        if i.x==spieler.x and i.y==spieler.y:
            gefunden=i
            break
    
    if not gefunden:
        return None
    
    if isinstance(gefunden, Waffe):
        _verarbeite_waffen_fund(spieler, gefunden, item_liste, map)
    else:
        _verarbeite_standart_item(spieler, gefunden, item_liste, map)
#code von Gemini 3 Pro

def _verarbeite_waffen_fund(spieler,waffe,item_liste,map):
    _zeige_popup(spieler,waffe)
    while True:
            if msvcrt.kbhit():
                taste = msvcrt.getch().lower()
#code von Gemini 3 Pro
                if taste== TASTE_J:
                    spieler.waffe=waffe
                    spieler.schaden=waffe.schaden
                    spieler.waffenname=waffe.name
                    neue_hp=spieler.getHP()//2
                    if neue_hp<1:
                        neue_hp=1
                    spieler.setHP(neue_hp)
                    _entferne_item_von_map(waffe,item_liste,map)
                    print(Farbe.GRUEN + '\n AUSGERÜSTET!' + Farbe.RESET)
                    time.sleep(1)
                    break
                elif taste==TASTE_N:
                    print(Farbe.ROT + '\n Nicht eingesammelt!' + Farbe.RESET)
                    time.sleep(1)
                    break

def _entferne_item_von_map(item,item_liste,map):
    if item in item_liste:
        item_liste.remove(item)
    map.grid[item.y][item.x]=BODEN

def _zeige_popup(spieler,neue_waffenoption):
    os.system('cls')
    print(Farbe.GELB + "========================================")
    print("          WAFFE GEFUNDEN!               ")
    print("========================================" + Farbe.RESET)
    print(f"\nNeue Waffe:    {neue_waffenoption.symbol} {neue_waffenoption.name}")
    print(f"Neuer Schaden: {neue_waffenoption.schaden}")

    if isinstance(neue_waffenoption, Schwert):
        print(Farbe.ROT + "EFFEKT:        HALBIERT DEINE HP!" + Farbe.RESET)
    elif isinstance(neue_waffenoption, Laserschwert):
        print(Farbe.BLAU + "EFFEKT:        Verbraucht 5 Batterie pro Schlag!" + Farbe.RESET)
        print(Farbe.BLAU + "               (Ohne Strom nur 1 Schaden)" + Farbe.RESET)
    elif isinstance(neue_waffenoption, Dolch):
        print(Farbe.GRUEN + "EFFEKT:        Heilt +2 HP pro Treffer!" + Farbe.RESET)
    elif isinstance(neue_waffenoption, Schwert):
        print(Farbe.ROT + "EFFEKT:        HALBIERT DEINE HP!" + Farbe.RESET)

    print("-" * 30)
    print(f"Aktuell:       {spieler.waffenname}")
    print(f"Aktueller DMG: {spieler.schaden}")
    print("\nMöchtest du die Waffe wechseln?")
    print("[J] Ja, nehmen!")
    print("[N] Nein, liegen lassen.")
#code von Gemini 3 Pro

def _verarbeite_standart_item(spieler,item,item_liste,map):
    if isinstance(item, Heilung):
        neue_hp = min(100, spieler.getHP() + item.wert)
        spieler.setHP(neue_hp)
    elif isinstance(item, Batterie):
        neue_bat = min(100, spieler.getBatterie() + item.wert)
        spieler.setBatterie(neue_bat)
    
    # Sofort entfernen, da verbraucht
    _entferne_item_von_map(item, item_liste, map)
#code von Gemini 3 Pro

def update_fahne(map,gegner_liste, ziel_koordinaten):
    ziel_x,ziel_y=ziel_koordinaten
#code von Gemini 3 Pro

    if len(gegner_liste)==0:
        map.grid[ziel_y][ziel_x]=ZIEL_GRÜN
        return True
    else:
        return False
    
def inputs_holen(spieler):
    dx, dy = 0, 0
    aktion = None # Kann sein: 'quit', 'save', 'load', 'cheat' oder None
    
    while msvcrt.kbhit():
        taste = msvcrt.getch().lower()
        
        if taste == TASTE_W: 
            dx = 0
            dy = -1
        elif taste == TASTE_S: 
            dx = 0
            dy = 1
        elif taste == TASTE_A: 
            dy = 0
            dx = -1
        elif taste == TASTE_D: 
            dy = 0
            dx = 1
        elif taste == TASTE_C:
            aktion = 'cheat'
        elif taste == TASTE_K:
            aktion = 'save'
        elif taste == TASTE_L:
            aktion = 'load'
        elif taste == TASTE_BEENDEN: 
            aktion = 'quit'
        
    return dx, dy, aktion
#code von Gemini 3 Pro

def verarbeite_zug(spieler, map, gegner_liste, item_liste, dx, dy):
    ziel_x = spieler.x + dx
    ziel_y = spieler.y + dy

    gekämpft_gegen = None

    # 1. Gegner Check
    gegner = next((g for g in gegner_liste if g.x == ziel_x and g.y == ziel_y), None)
    
    if gegner:
        game_over = kampf_abwickeln(spieler, gegner, gegner_liste, map)
        if game_over: return 'lost'

        if isinstance(gegner, Golem) or gegner.name == "Golem":
            gekämpft_gegen = None 
        else:
            gekämpft_gegen = gegner 

    # 2. Ziel Check
    elif map.grid[ziel_y][ziel_x] == ZIEL_GRÜN: 
        return 'won'
    elif map.grid[ziel_y][ziel_x] == ZIEL_ROT:
        print("Das Tor ist noch zu!")
        return 'running'
    elif not gegner: 
        # 3. Bewegung und Lava-Check
        spieler.bewegen(dx, dy, map)
        spieler.setBatterie(spieler.getBatterie() - 1)
        item_einsammeln(spieler, item_liste, map)

        # NEU: LAVA CHECK
        # Wenn wir auf einem Lava-Feld stehen
        if map.grid[spieler.y][spieler.x] == LAVA:
            print(Farbe.BG_ORANGE + Farbe.WEISS + "!!! IN LAVA GEFALLEN !!!" + Farbe.RESET)
            print(Farbe.ROT + "-15 HP | -10 Batterie" + Farbe.RESET)
            time.sleep(1) 
            print("")
            print("")

            # Schaden zufügen
            spieler.setHP(spieler.getHP() - 15)
            spieler.setBatterie(spieler.getBatterie() - 10)

            # Lava kühlt ab (wird wieder Boden), damit man nicht sofort stirbt
            map.grid[spieler.y][spieler.x] = BODEN

    spieler.züge += 1 

    spieler_tot = gegner_runde_ausführen(spieler, gegner_liste, map, pausierender_gegner=gekämpft_gegen)
    
    if spieler_tot:
        return 'lost'
    
    # Check ob man durch Lava gestorben ist
    if spieler.getHP() <= 0:
        return 'lost'
    
    return 'running'
#code von Gemini 3 Pro

def start_screen():
    os.system('cls')
    print(Farbe.GELB + "==========================================")
    print("      DUNGEON CRAWLER - ENDLOS MODUS      ")
    print("==========================================" + Farbe.RESET)
    print("\nSteuerung: W, A, S, D")
    print("Ziel: Besiege alle Gegner, um das Tor zu öffnen.")
    print("      HP und Batterie werden ins nächste Level mitgenommen!")
    
    # NEU: Warnhinweis für Lava
    print(Farbe.ROT + "\nACHTUNG: Vermeide die Lava (orangene Felder)!" + Farbe.RESET)
    
    print("\nDrücke eine TASTE zum Starten...")
    warte_auf_eingabe()
#code von Gemini 3 Pro

def warte_auf_eingabe():
    while msvcrt.kbhit():
            msvcrt.getch()
    msvcrt.getch()
#code von Gemini 3 Pro

def gegner_runde_ausführen(spieler,gegner_liste,map, pausierender_gegner=None):
    for i in gegner_liste:
        if i==pausierender_gegner:
            continue

        state=i.verfolgen(spieler,map,spieler.züge)
        if state:
            print(Farbe.ROT + state + Farbe.RESET)

    if spieler.getHP()<=0:
        return True
    else:
        return False



print('Das Spiel muss in "spiel.py" gestartet werden!')
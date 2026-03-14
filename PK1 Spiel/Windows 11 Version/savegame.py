import pickle
import os

SPEICHERDATEI="Savegame.dat"
def spiel_speichern(spieler,map,gegner_liste,item_liste,koordinaten,level):
    daten={
        "spieler":spieler,
        "map":map,
        "gegner":gegner_liste,
        "items":item_liste,
        "koordinaten":koordinaten,
        "level":level
    }
    try:
        with open(SPEICHERDATEI,"wb") as f:
            pickle.dump(daten,f)
        return True
    except:
        print("Fehler beim Speichern!")
        return False
#code von Gemini 3 Pro

def spiel_laden():
    if not os.path.exists(SPEICHERDATEI):
        return None
    
    try:
        with open(SPEICHERDATEI,"rb") as f:
            daten=pickle.load(f)
        return daten
    except:
        print("Fehler beim Laden!")
        return None
#code von Gemini 3 Pro
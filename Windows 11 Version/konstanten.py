from farben import Farbe

import sys
sys.stdout.reconfigure(encoding='utf-8')
#code von Gemini 3 Pro zur Behebung von "UnicodeEncodeError"

MAP_BREITE=80
MAP_HÖHE=40
LICHT_RADIUS=10

WAND=Farbe.BG_WEISS + "  " + Farbe.RESET
SPIELER =Farbe.BG_GRAU + Farbe.GELB +  "\uC6C3" + Farbe.RESET #Koreanisches Zeichen was wie ein Männchen aussieht
BODEN=Farbe.BG_GRAU + "  " + Farbe.RESET
ZIEL_ROT=Farbe.BG_GRAU + Farbe.ROT + "\u2691 " + Farbe.RESET #Flagge
ZIEL_GRÜN=Farbe.BG_GRAU + Farbe.GRUEN + "\u2691 " + Farbe.RESET #Flagge
DUNKELHEIT=Farbe.BG_SCHWARZ + "  " + Farbe.RESET
ZOMBIE=Farbe.BG_GRAU + "🧟" + Farbe.RESET
GEIST=Farbe.BG_GRAU + "👻" + Farbe.RESET
SKELETT=Farbe.BG_GRAU + "💀" + Farbe.RESET
HERZ=Farbe.BG_GRAU +Farbe.ROT + "♥️" + Farbe.RESET
BATTERIE=Farbe.BG_GRAU + "🔋" + Farbe.RESET
SCHWERT=Farbe.BG_GRAU + Farbe.BLAU + "⚔️" + Farbe.RESET
FAUST=Farbe.BG_SCHWARZ + Farbe.GELB + "👊" + Farbe.RESET
GOLEM=Farbe.BG_GRAU + "🗿" + Farbe.RESET
LASERSCHWERT=Farbe.BG_GRAU + "🔦" + Farbe.RESET
DOLCH=Farbe.BG_GRAU + "🗡" + Farbe.RESET
LAVA=Farbe.BG_ORANGE + "  " + Farbe.RESET

TASTE_W=b'w'
TASTE_A=b'a'
TASTE_S=b's'
TASTE_D=b'd'
TASTE_BEENDEN=b'b'
TASTE_J=b'j'
TASTE_N=b'n'
TASTE_C=b'c'
TASTE_X=b'x'
TASTE_K=b'k' 
TASTE_L=b'l'



print('Das Spiel muss in "spiel.py" gestartet werden!')
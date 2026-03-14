from farben import Farbe

import sys
sys.stdout.reconfigure(encoding='utf-8')
#code von Gemini 3 Pro zur Behebung von "UnicodeEncodeError"

MAP_BREITE=80
MAP_HÖHE=40
LICHT_RADIUS=10

WAND=Farbe.BG_WEISS + "  " + Farbe.RESET
SPIELER =Farbe.BG_GRAU + Farbe.GELB +  "☺ " + Farbe.RESET 
BODEN=Farbe.BG_GRAU + "  " + Farbe.RESET
ZIEL_ROT=Farbe.BG_GRAU + Farbe.WEISS + "P " + Farbe.RESET 
ZIEL_GRÜN=Farbe.BG_GRAU + Farbe.GRUEN + "p " + Farbe.RESET 
DUNKELHEIT=Farbe.BG_SCHWARZ + "  " + Farbe.RESET
ZOMBIE=Farbe.BG_GRAU + Farbe.ROT + "Z " + Farbe.RESET
GEIST=Farbe.BG_GRAU + Farbe.ROT + "Ge" + Farbe.RESET
SKELETT=Farbe.BG_GRAU + Farbe.ROT + "Sk" + Farbe.RESET
HERZ=Farbe.BG_GRAU +Farbe.BLAU + "H " + Farbe.RESET
BATTERIE=Farbe.BG_GRAU + Farbe.BLAU + "B " + Farbe.RESET
SCHWERT=Farbe.BG_GRAU + Farbe.BLAU + "Sc" + Farbe.RESET
FAUST=Farbe.BG_SCHWARZ + Farbe.BLAU + "F " + Farbe.RESET
GOLEM=Farbe.BG_GRAU + Farbe.ROT+ "Go" + Farbe.RESET
LASERSCHWERT=Farbe.BG_GRAU + Farbe.BLAU + "L " + Farbe.RESET
DOLCH=Farbe.BG_GRAU + Farbe.BLAU + "D" + Farbe.RESET
LAVA=Farbe.BG_ORANGE + "  " + Farbe.RESET
#die symbole sollten eigentlich passende Emogies oder Unicode zeichen sein, diese können in cmd jedoch von windows 10 nicht angezeigt werden

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
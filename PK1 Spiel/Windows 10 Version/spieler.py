from konstanten import *
from map import *

class Spieler:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.__hp=100
        self.__batterie=100
        self.züge=0
        self.schaden=1
        self.waffe=None
        self.waffenname="Faust"
    
    def setHP(self,neue_hp):
            self.__hp=neue_hp

    def getHP(self):
        return self.__hp
    
    def setBatterie(self, neue_batterie):
        if neue_batterie<=100 and neue_batterie>=0 and type(neue_batterie)==int:
            self.__batterie=neue_batterie
    
    def getBatterie(self):
        return self.__batterie

    def bewegen(self, dx, dy, karte_objekt):
        neues_x = self.x + dx
        neues_y = self.y + dy
        if not karte_objekt.ist_blockiert(neues_x, neues_y):
            self.x = neues_x
            self.y = neues_y
#Code von Gemini 3 Pro generiert



print('Das Spiel muss in "spiel.py" gestartet werden!')
from konstanten import HERZ, BATTERIE, SCHWERT, LASERSCHWERT, DOLCH
from spieler import *

class Item():
    def __init__(self,x,y,symbol,name):
        self.x = x
        self.y = y
        self.symbol = symbol
        self.name = name

class Heilung(Item):
    def __init__(self,x,y):
        super().__init__(x,y,HERZ, "Heilung")
        self.wert=50

class Batterie(Item):
    def __init__(self,x,y):
        super().__init__(x,y,BATTERIE, "Batterie")
        self.wert=100

class Waffe(Item):
    def __init__(self,x,y,symbol,name,schaden):
        super().__init__(x,y,symbol,name)
        self.schaden=schaden

class Schwert(Waffe):
    def __init__(self,x,y):
        super().__init__(x,y,SCHWERT,"Schwert",3)

class Laserschwert(Waffe):
    def __init__(self,x,y):
        super().__init__(x,y,LASERSCHWERT,"Laserschwert",100)

class Dolch(Waffe):
    def __init__(self,x,y):
        super().__init__(x,y,DOLCH,"Dolch",1)
        self.treffer=0



print('Das Spiel muss in "spiel.py" gestartet werden!')
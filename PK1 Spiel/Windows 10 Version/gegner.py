from konstanten import ZOMBIE, GEIST,SKELETT, BODEN, GOLEM

class Gegner():
    def __init__(self,x,y,hp,symbol,name,stärke,geschwindigkeit):
        self.x = x
        self.y = y
        self.hp = hp
        self.symbol = symbol
        self.name = name
        self.stärke=stärke
        self.geschwindigkeit=geschwindigkeit

    def schaden_nehmen(self,schaden):
        self.hp-=schaden

    def verfolgen(self, spieler, map, zug_nummer): 
        # 1. Darf ich laufen?
        if not self._ist_am_zug(zug_nummer):
            return None 

        # 2. Wohin will ich?
        ziel_x, ziel_y = self._berechne_ziel(spieler)

        # 3. Mach es!
        return self._schritt_ausführen(ziel_x, ziel_y, spieler, map)
#code von Gemini 3 Pro

    def _ist_am_zug(self, zugnummer):
        return zugnummer%self.geschwindigkeit==0
    
    def _berechne_ziel(self,spieler):
        # Simpler Algorithmus: Gehe in die Richtung, wo der Abstand am größten ist
        dx = 0
        dy = 0
        
        # X-Richtung bestimmen
        if self.x < spieler.x: dx = 1
        elif self.x > spieler.x: dx = -1
        
        # Y-Richtung bestimmen
        if self.y < spieler.y: dy = 1
        elif self.y > spieler.y: dy = -1
        
        # Abstände vergleichen
        dist_x = abs(self.x - spieler.x)
        dist_y = abs(self.y - spieler.y)

        # Entscheidung: Horizontal oder Vertikal laufen?
        if dist_x > dist_y:
            return self.x + dx, self.y
        else:
            return self.x, self.y + dy
        
    def _schritt_ausführen(self, ziel_x, ziel_y, spieler, map):
        # Fall A: Angriff
        if ziel_x == spieler.x and ziel_y == spieler.y:
            schaden = self.stärke
            spieler.setHP(spieler.getHP() - schaden)
            return # Fertig

        # Fall B: Laufen
        if map.grid[ziel_y][ziel_x] == BODEN:
            self._aktualisiere_Position(ziel_x, ziel_y, map)
#code von Gemini 3 Pro

    def _aktualisiere_Position(self,neu_x,neu_y,map):
        map.grid[self.y][self.x]=BODEN
        self.x=neu_x
        self.y=neu_y
        map.grid[self.y][self.x]=self.symbol

class Zombie(Gegner):
    def __init__(self,x,y):
        super().__init__(x,y,3,ZOMBIE, "Zombie",15,3)

class Geist(Gegner):
    def __init__(self,x,y):
        super().__init__(x,y,1,GEIST,"Geist",5,1)

class Skelett(Gegner):
    def __init__(self,x,y):
        super().__init__(x,y,2,SKELETT,"Skelett",10,2)

class Golem(Gegner):
    def __init__(self,x,y):
        super().__init__(x,y,20,GOLEM,"Golem",25,2)
        self.charge=0

    def _schritt_ausführen(self,ziel_x,ziel_y,spieler,map):
        if ziel_x==spieler.x and ziel_y==spieler.y:
            self.charge+=1
        
            if self.charge%3==0:
                schaden=self.stärke
                spieler.setHP(spieler.getHP()-schaden)
                return "Der Golem greift an"
            else:
                return "Golem holt aus"
        else:
            super()._schritt_ausführen(ziel_x,ziel_y,spieler,map)
            return None




print('Das Spiel muss in "spiel.py" gestartet werden!')
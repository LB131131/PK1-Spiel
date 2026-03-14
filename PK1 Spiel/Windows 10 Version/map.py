from konstanten import *
import random

class Map:
    def __init__(self, breite, höhe, level=1):
        self.breite=breite
        self.höhe=höhe
        self.grid=[]
        self.__level=level
        self.wand_wahrscheinlichkeit=0.1+(level*0.01)
        #verhindert, dass es übermäßig viele wände gibt
        if self.wand_wahrscheinlichkeit>0.35:
            self.wand_wahrscheinlichkeit=0.35
        self.kartengenerator()

    def getLevel(self):
        return self.__level
    
    def setLevel(self, neues_level):
        if neues_level>=1 and type(neues_level)==int:
            self.__level=neues_level

    def kartengenerator(self):
        #y-achse durchlaufen
        for y in range (0,self.höhe):
            zeile=[]
            #x-achse durchgehen
            for x in range (0,self.breite):
                #am rand sollen nur wände sein
                if y==0 or y==self.höhe-1 or x==0 or x==self.breite-1:
                    zeile.append(WAND)
                else:
                    if random.random()<=self.wand_wahrscheinlichkeit:
                        zeile.append(WAND)
                    else:
                        zeile.append(BODEN) 
            self.grid.append(zeile)
        
        self._nur_größte_höhle_behalten()

        self.lava_platzieren()

    def lava_platzieren(self):
        lava_wahrscheinlichkeit=0.01+(self.__level*0.005)
        for y in range(1,self.höhe-1):
            for x in range(1,self.breite-1):
                if self.grid[y][x]==BODEN:
                    if random.random()<lava_wahrscheinlichkeit:
                        self.grid[y][x]=LAVA

    def ist_blockiert(self, x, y):
        if x < 0 or x >= self.breite or y < 0 or y >= self.höhe:
            return True #feld ist außerhalb der map 
        if self.grid[y][x] == WAND:
            return True #feld ist duch eine wand blockiert
        return False
#code von Gemini 3 Pro generiert

    def _nur_größte_höhle_behalten(self):
        visited = set()
        alle_gruppen = []

        # Scanne die ganze Map nach Boden-Gruppen
        for y in range(1, self.höhe - 1):
            for x in range(1, self.breite - 1):
                if self.grid[y][x] == BODEN and (x, y) not in visited:
                    # Neue Gruppe gefunden! -> Erforschen (Flood Fill)
                    gruppe = []
                    queue = [(x, y)]
                    visited.add((x, y))
                    
                    while queue:
                        cx, cy = queue.pop(0)
                        gruppe.append((cx, cy))
                        
                        # Nachbarn checken (oben, unten, links, rechts)
                        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                            nx, ny = cx + dx, cy + dy
                            if 0 < nx < self.breite-1 and 0 < ny < self.höhe-1:
                                if self.grid[ny][nx] == BODEN and (nx, ny) not in visited:
                                    visited.add((nx, ny))
                                    queue.append((nx, ny))
                    alle_gruppen.append(gruppe)

        if not alle_gruppen: 
            return # Sollte nicht passieren (Map wäre komplett voll)

        # Die größte Gruppe gewinnt
        groesste = max(alle_gruppen, key=len)
        groesste_set = set(groesste)

        # Alles, was NICHT zur größten Gruppe gehört, wird zugemauert
        for y in range(1, self.höhe - 1):
            for x in range(1, self.breite - 1):
                if self.grid[y][x] == BODEN and (x, y) not in groesste_set:
                    self.grid[y][x] = WAND
#code von Gemini 3 Pro




print('Das Spiel muss in "spiel.py" gestartet werden!')
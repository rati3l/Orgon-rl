import curses
from character import Postac
from random import randint


class Kratka:
    def __init__(self,yx, widocznosc=True, passable=False):
        self.yx = yx
        self.widocznosc = widocznosc
        self.passable = passable
    def __eq__(self,other):
        return self.yx == other.yx


class Mapa:

    def __init__(self, okno_mapy, postac):
        self.okno_mapy = okno_mapy
        self.postac = postac
        self.dostepne_kratki = [Kratka([y,x]) for y in range \
                                (1,self.okno_mapy.getmaxyx()[0] -1) \
                                for x in range (1,self.okno_mapy.getmaxyx()[1] -1) ]



    def stworz_pokoj(self):
        startx = randint(1, self.okno_mapy.getmaxyx()[0] -16)
        starty = randint(1, self.okno_mapy.getmaxyx()[1] -16) 
        x = startx + randint(7,15)
        y = starty + randint(7,15)
        return [Kratka([i,j]) for i in range(startx, x) for j in range(starty,  y)]
    
    def pokoje(self, ile):
        self.pokoje = []
        for i in range(100):
            temp = self.stworz_pokoj()
            for item in temp:
                for pokojj in self.pokoje:
                    if item not in pokojj:
                        self.pokoje.append(temp)
    
    
    
    def rysuj(self):
        self.okno_mapy.erase()
        self.okno_mapy.box()

        for item in self.dostepne_kratki:
            if item.widocznosc == True:
                self.okno_mapy.addch(*item.yx, '#')
        for item in self.pokoje:
            for item2 in item:
                self.okno_mapy.addch(*item2.yx, ' ')
        self.okno_mapy.addch(*self.postac.yx, '@')
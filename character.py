import curses

class Postac:
    
    def __init__(self, y,x, okno_mapy):
        self.yx = [int(y/2), int(x/2)]
        self.okno_mapy = okno_mapy


    def ruch(self, key):
        if key == curses.KEY_UP:
            self.yx[0]-=1
            
        if key == curses.KEY_DOWN:
            self.yx[0]+=1

        if key == curses.KEY_RIGHT:
            self.yx[1]+=1

        if key == curses.KEY_LEFT:
            self.yx[1]-=1
    
    def rysuj(self):
        self.okno_mapy.delch(*self.yx)
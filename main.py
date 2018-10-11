#! /usr/bin/python3
import curses
from curses import wrapper
from character import  Postac
from mapa import Mapa

def main(ekran):
    curses.curs_set(0)

    ekran.clear()
    ekran_y = 40
    ekran_x = 100

    okno_mapy = curses.newwin(ekran_y, ekran_x-15,0,0)
    okno_eq = curses.newwin(ekran_y, ekran_x-60,0,ekran_x-16)
    
    
    
    curses.beep()
    okno_eq.border(0,0,0,0,curses.ACS_TTEE,0,curses.ACS_BTEE,0)


    if (curses.LINES -1 < ekran_y) | (curses.COLS -1 < ekran_x):
        return ("Okno terminala jest za male!")


    postac = Postac(*okno_mapy.getmaxyx(), okno_mapy)
    mapa = Mapa(okno_mapy, postac)
    
    mapa.stworz_pokoj()

    while True:
        
        mapa.rysuj()
        ekran.refresh()
        okno_mapy.refresh()
        okno_eq.refresh()
        
        strzalka = ekran.getch()
        
        postac.ruch(strzalka)
        
        



    ekran.getch()

if __name__ == "__main__":
    x = wrapper(main) 
    if x:
        print(x)

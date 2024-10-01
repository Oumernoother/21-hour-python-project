import curses
from curses import wapper

def main(stdscr):
    stdscr.clear()
    stdscr.addstr("Hello word!")
    stdscr.refresh()
    stdscr.getkey()
wapper(main)
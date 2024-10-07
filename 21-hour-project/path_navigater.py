import curses
from curses import wrapper
import queue
import time

maze = [
    ['#','#','#','#','#','o','#','#','#'],
    ['#',' ',' ',' ',' ',' ',' ',' ','#'],
    ['#',' ','#','#',' ','#','#',' ','#'],
    ['#',' ','#',' ',' ',' ','#',' ','#'],
    ['#',' ','#',' ','#',' ','#',' ','#'],
    ['#',' ','#',' ','#',' ','#',' ','#'],
    ['#',' ','#',' ','#',' ','#','#','#'],
    ['#',' ',' ',' ',' ',' ',' ',' ','#'],
    ['#','#','#','#','#','#','#','x','#'],
]

def print_maze(maze, stdscr, path=[]):
    BULE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            stdscr.addstr(i,j*2, value)

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)

    stdscr.clear()
    # stdscr.addstr(0,0, "hello", curses.init_pair(1))
    print_maze(maze, stdscr)
    stdscr.refresh()
    stdscr.getch()
wrapper(main)
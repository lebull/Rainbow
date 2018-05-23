# This

#Tetris Psudo
import sys
import time
import random

from screen import Screen, Color

from memory import MemorySpace


#The screen, colors and all, should be represented by 800 (128 + 64 + 8) bits
#0b11001000 (0xC8)
screen = Screen((10, 20))

memory = MemorySpace(4096, 16)

#------------------------------------------
#    Begin Psudocode
#------------------------------------------

#Block Type Definitions

SQUARE = 0             #def
NUM_SQUARE = 1         #def
SQUARE_COLOR = 0
SQUARE_SHAPES = [
    "     XX  XX     "
]

ELL = 1                 #def
NUM_ELL = 2             #def
ELL_COLOR = 1           #def

BELL = 2                #def
NUM_BELL = 2            #def
BELL_COLOR = 2          #def

ZIG = 3                 #def
NUM_ZAG = 2             #def
ZIG_COLOR = 3           #def

ZAG = 4                 #def
NUM_ZAG = 2             #def
ZAG_COLOR = 4           #def

TEE = 5                 #def
NUM_TEE = 4             #def
TEE_COLOR = 5           #def

LINE = 6                #def
NUM_LINE = 4            #def
LINE_COLOR = 6          #def
LINE_SHAPES = [
#   |.   .   .   .   |
    "    XXXX        ",
    "  X   X   X   X ",
    "        XXXX    ",
    " X   X   X   X  "
]



blocks = {
    "ell": [],
    "bell": [],
    "tee": [],
    "zig": [],
    "zag": []
}

#Should be handled by its own opcode
def setScreenPixel(pos, color):
    screen.data[pos[0]][pos[1]] = color

#16 bit var
currentShape = {
    "shape": LINE, #3
    "orientation": 0,     #2
    "pos": (0, 0)         #5, 6
}


def blitBlock(shape, orientation, pos, unblit):

    #case
    if(shape == LINE):
        shapeData = LINE_SHAPES[orientation]

    i = 0
    while i < 16:
        targetPos = (pos[0] + i/4, pos[1] + i%4)
        if(shapeData[i] == "X"):
            if(unblit):
                color = Color.BG_DEFAULT
            else:
                color = Color.BG_RED
            #should be handled by its own opcode
            setScreenPixel((targetPos[1], targetPos[0]), color)
        i+=1

#Rotates the currentShape if allowed.  Does nothing otherwise.
def rotate(direction):
    global currentShape

    #Squares don't rotate xD
    if(currentShape["shape"] == SQUARE):
        return


#Return a 4x4 grid of occupied spots on the board, encoded
# as 16 bits.  OOBs will be considered "occupied".
def getQuartFromBoard(pos):

    pass

#Returns true if any two corrisponding spots of two quarts are both occupied.
#At lower levels, this should be the same as a series of ANDS
def quartsConflict(quart1, quart2):
    pass


#Main execution
for i in range(8):
    currentShape["orientation"] = i % NUM_LINE
    currentShape["pos"] = (currentShape["pos"][0], currentShape["pos"][1] + 1)

    blitBlock(
        currentShape["shape"],
        currentShape["orientation"],
        currentShape["pos"],
        False)
    screen.printout()

    time.sleep(0.5)

    blitBlock(
        currentShape["shape"],
        currentShape["orientation"],
        currentShape["pos"],
        True)

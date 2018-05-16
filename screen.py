import random
import sys

class ScreenShapes(object):
    SINGLE = " "
    DOUBLE = "  "

class ScreenColors(object):
    PX_DEFAULT = 0
    PX_BLACK = 1
    PX_RED = 8
    PX_GREEN = 9
    PX_MAG = 10
    PX_CYAN = 11
    PX_LIGHTRED = 12
    PX_LIGHTYELLOW = 13
    PX_LIGHTGREEN = 14
    PX_LIGHTBLUE = 15

    BG_DEFAULT="49"
    BG_BLACK= "40"
    #BG_WHITE=?
    BG_RED= "41"
    BG_GREEN="42"
    BG_YELLOW="43"
    BG_BLUE="44"
    BG_MAG="45"
    BG_CYAN="46"

    BG_GREY = "100"

    BG_LIGHTRED = "101"
    BG_LIGHTYELLOW = "102"
    BG_LIGHTGREEN = "103"
    BG_LIGHTBLUE = "104"

    @classmethod
    def random(cls):
        return random.choice([
            cls.BG_MAG,         #1000
            cls.BG_GREEN,       #1001
            cls.BG_CYAN,        #1010
            cls.BG_LIGHTRED,    #1011
            cls.BG_LIGHTYELLOW, #1100
            cls.BG_LIGHTGREEN,  #1101
            cls.BG_LIGHTBLUE]   #1110
        )

    @classmethod
    def pxToScreencolor(cls, pxBits):
        return cls.BG_MAG

class Screen(object):

    shape = ScreenShapes.DOUBLE

    def __init__(self, size=(64, 64)):
        self.size = size
        self.data = [[0 for x in range(self.size[0])] for y in range(self.size[1])]
        self.outputString = ""
        self.boarderColor = ScreenColors.BG_BLACK

    def _pushOutputString(self, data):
        self.outputString += data

    def clear(self):
        sys.stdout.write("\033[2J\033[H")
        self.outputString = ""

    def setColor(self, color=None):
        if(not color):
            color='39'

        self._pushOutputString("\033[{}m".format(color))
        #sys.stdout.write("\033[41m  \033[0m\n")

    def clearColor(self):
        self._pushOutputString("\033[{}m".format("39"))
        self._pushOutputString("\033[{}m".format("49"))

    def write(self, text, colors=None):
        self.clearColor()

        try:
            for color in colors:
                self.setColor(color)
        except:
            self.setColor(colors)

        self._pushOutputString(text)



    def printout(self):
        self.clear()
        self.write(self.shape * (self.size[0] + 2), [self.boarderColor])
        self.write("\n")
        for l in self.data:
            self.write(self.shape, [self.boarderColor])
            for data in l:
                if(data):
                    self.write(self.shape, [data])
                else:
                    self.write(self.shape)

            self.write(self.shape, [self.boarderColor])
            self.write("\n")
        self.write(self.shape * (self.size[0] + 2), [self.boarderColor])
        self.write("\n")
        self.clearColor()

        sys.stdout.write(self.outputString)

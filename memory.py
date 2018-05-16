from screen import Screen, ScreenColors

from bitarray import bitarray

import math, random



class MemorySpace(object):
    def __init__(self, totalBits, wordSize):
        self.data = bitarray(totalBits*wordSize)#[0 for i in range(totalBits)]
        self.totalBits = totalBits
        self.wordSize = wordSize
        self.allocations = {}

    def __len__(self):
        return len(self.data)/self.wordSize

    def getBitIndexesFromAddress(self, address, count=None):
        if(not count):
            count = self.wordSize
        startBitNumber = address * self.wordSize
        endBitNumber = startBitNumber + count
        return (startBitNumber, endBitNumber)

    def readWord(self, address):
        bitNum = self.getBitIndexesFromAddress(address)
        return int(self.data[bitNum[0] : bitNum[1]].to01(), 2)

    def writeWord(self, address, data):
        bitNum = self.getBitIndexesFromAddress(address)

        newData = bitarray(self.wordSize)
        dataString = bin(int(data))[2:]
        newData[-len(dataString):] = bitarray(dataString)
        #newData.frombytes(data)
        print newData
        self.data[bitNum[0]: bitNum[1]] = newData

    def getMaxAddress(self):
        return self.totalBits/sel.wordSize

    def allocate(self, label, words):
       self.allocations[label]

    def readAllocated(self, label, words):
       pass

    #writeAllocated(self, label, data)
    #   pass

class VisualMemory(MemorySpace):
    def __init__(self, wordsPerRow, *args, **kwargs):
        super(VisualMemory, self).__init__(*args, **kwargs)
        rowWidth = self.wordSize * wordsPerRow
        numRows = float(self.totalBits)/rowWidth
        numRows = int(math.ceil(numRows))
        self.screen = Screen((rowWidth, numRows))

    def bitToScreenPos(self):
        pass

    def draw(self):
        for t in range(100):
            pos = (random.randint(0, self.screen.size[0]-1), random.randint(0, self.screen.size[1]-1))
            self.screen.data[pos[1]][pos[0]] = ScreenColors.random()
        self.screen.printout()

if __name__ == "__main__":
    import unittest

    class TestMemorySpace(unittest.TestCase):
        def testCreate(self):
            wordSize = 16
            space = MemorySpace(0xFFFF, wordSize)
            self.assertEqual(len(space)/wordSize, 0xFFF)


        def testReadWriteWord(self):
            space = MemorySpace(0xFFFF, 16)
            data = 0x1A2B
            address = 0xF000
            space.writeWord(address, data)
            readData = space.readWord(address)
            self.assertEqual(data, readData)

        def testReadWriteAllocation(self):
            space = MemorySpace(0xFFFF, 16)
            space.allocate("alloc", 0xC8)
            self.assertEqual(space.readAllocated, readData)


        #TODO:
        # Test writing a value that is too large
        # Test writing to an address that is out of range

        #If you try to allocate a space with an existing name, raise an error
        #If you try to allocate space beyond the size of the memorySpace, raise an overflow error

        #def highlightAllocated(self, label):
        #   pass


    #
    v = VisualMemory(4, 4096, 16).draw()

    #unittest.main()

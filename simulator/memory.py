from screen import Screen, Color
from bitarray import bitarray
import math, random


def _dataToBits(data):
    newData = bitarray()
    dataString = bin(int(data))[2:]
    return bitarray(dataString)

class _Allocation(object):
    def __init__(self, name, size, startAddress, parentSpace):
        self.name = name
        self.size = size
        self.startAddress = startAddress
        self.parentSpace = parentSpace


    def writeData(self, data):
        pass

    def getEndAddress(self):
        return self.startAddress + self.size

class MemorySpace(object):
    def __init__(self, totalBits, wordSize):
        self.data = bitarray(totalBits*wordSize)#[0 for i in range(totalBits)]
        self.totalBits = totalBits
        self.wordSize = wordSize
        self.allocations = []

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
        newWord = bitarray(self.wordSize)
        newData = _dataToBits(data)
        newWord[-len(newData):] = newData
        self.data[bitNum[0]: bitNum[1]] = newWord

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
            self.screen.data[pos[1]][pos[0]] = Color.random()
        self.screen.printout()

if __name__ == "__main__":
    import unittest

    class TestAllocation(unittest.TestCase):
        def setUp(self):
            self.wordSize = 0x10
            self.spaceSize = 0xFFFF
            self.memorySpace = MemorySpace(self.spaceSize, self.wordSize)


        def testCreate(self):
            name = "TestAlloc"
            allocationSize = 0xFF
            startAddress = 0x00

            allocation = _Allocation(name, allocationSize, startAddress, self.memorySpace)
            self.assertEqual(allocation.name, name)
            self.assertEqual(allocation.size, allocationSize)
            self.assertEqual(allocation.parentSpace, self.memorySpace)
            self.assertEqual(allocation.startAddress, startAddress)

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

        # def testReadWriteAllocation(self):
        #     space = MemorySpace(0xFFFF, 16)
        #     space.allocate("alloc", 0xC8)
        #     self.assertEqual(space.readAllocated, readData)


        #TODO:
        # Test writing data that is too large
        # Test writing to an address that is out of range

        #If you try to allocate a space with an existing name, raise an error
        #If you try to allocate space beyond the size of the memorySpace, raise an overflow error

        #def highlightAllocated(self, label):
        #   pass


    #
    #v = VisualMemory(4, 4096, 16).draw()

    unittest.main()

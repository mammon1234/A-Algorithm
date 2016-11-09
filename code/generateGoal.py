import cell
import random
class generateGoal(object):
    def __init__(self,MATRIX):
        self.Matrix = MATRIX
    def generate(self):
        while 1:
            startRow = self.generateRowPoint()
            startColumn = self.generateColumnPoint()
            endRow = self.generateRowPoint()
            endColumn = self.generateColumnPoint()
            if((not self.Matrix[startRow][startColumn].isBlocked()) and(not self.Matrix[endRow][endColumn].isBlocked())):
                if(abs(startRow - endRow)+abs(startColumn-endColumn))>=100:
                    #print str(startRow)+","+str(startColumn)+"[][]"+str(endRow)+","+str(endColumn)
                    #print self.Matrix[startRow][startColumn].getState()
                    #print self.Matrix[endRow][endColumn].getState()
                    break;
        return (startRow,startColumn,endRow,endColumn)
    def generateRowPoint(self):
        point = random.randint(0, 40)
        if (point >= 20):
            point = 119 + (20 - point)
        return point

    def generateColumnPoint(self):
        point = random.randint(0, 40)
        if (point >= 20):
            point = 159 + (20 - point)
        return point
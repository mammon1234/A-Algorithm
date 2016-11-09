import cell
class pathsave(object):
    def __init__(self,MATRIX,ENDROW,ENDCOLUMN):
        self.Matrix = MATRIX
        self.ENDROW = ENDROW
        self.ENDCOLUMN =ENDCOLUMN

    def savefile(self):
        curRow = self.ENDROW
        curColumn = self.ENDCOLUMN
        f = open('path.txt', 'w+')
        f.write(str(self.Matrix[curRow][curColumn].getFvalue())+"\r\n")
        while (curRow, curColumn) != self.Matrix[curRow][curColumn].getParent():
            #print str(curRow)+"[]"+str(curColumn)
            f.write("("+str(curRow)+","+str(curColumn)+")"+ "\r\n")
            (curRow, curColumn) = self.Matrix[curRow][curColumn].getParent()
        f.close()
import cell
class mapSave(object):
    def __init__(self,MATRIX,STARTROW,STARTCOLUMN,ENDROW,ENDCOLUMN,HARDCENTER):
        self.Matrix = MATRIX
        self.STARTROW = STARTROW
        self.STARTCOLUMN = STARTCOLUMN
        self.ENDROW = ENDROW
        self.ENDCOLUMN =ENDCOLUMN
        self.HARDCENTER = HARDCENTER

    def save(self):
        f = open('map.txt', 'w+')
        f.write(str(self.STARTROW)+","+str(self.STARTCOLUMN)+"\r\n")
        f.write(str(self.ENDROW) + "," + str(self.ENDCOLUMN) + "\r\n")
        for k in self.HARDCENTER:
            f.write(str(k[0]) + "," + str(k[1]) + "\r\n")
        f.write(str(120)+","+str(160)+"\r\n")
        f.close();
        f = open('map.txt', 'a+')
        for row in range(120):
            for column in range(160):
                if(self.Matrix[row][column].getHighWayIndex() != 0):
                    f.write(str(self.Matrix[row][column].getState())+str(self.Matrix[row][column].getHighWayIndex())+",")
                else:
                    f.write(str(self.Matrix[row][column].getState())+",")
            f.write("\r\n")
        f.close()
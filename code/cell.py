class cell(object):
    """
    A cell in a grid. Cells have the
    following properties:
    Attributes:
        isBlocked: Boolean value indicating whether a cell is blocked or not
    """

    def __init__(self, r, c):
        #Return a cell object with initial values.
        self.row = r
        self.column = c
        self.state = 1
        self.highwayIndex = 0;
        self.Fvalue=float('inf')
        self.Gvalue=float('inf')
        self.Hvalue =float('inf')
        self.parent=(r,c)


    def setState(self,value):
        self.state = value
    def getState(self):
        return self.state

    def setHard(self):
        #Sets the cell blocked value
        self.state = 2

    def isHard(self):
        return self.state == 2

    def setHighway(self,index):
        if(self.state == 1):
            self.state = 'a'
        if(self.state == 2):
            self.state = 'b'
        self.highwayIndex = index
    def getHighWayIndex(self):
        return self.highwayIndex

    def isHighway(self):
        return (self.state == 'a') or (self.state == 'b')

    def setBlocked(self):
        #Sets the cell blocked value
        self.state = 0

    def isBlocked(self):
        #Returns the value of blocked
        return self.state == 0

    def setFvalue(self,f):
        self.Fvalue = f
    def getFvalue(self):
        return self.Fvalue

    def setHvalue(self,h):
        self.Hvalue =h
    def getHvalue(self):
        return self.Hvalue

    def setGvalue(self,g):
        self.Gvalue =g

    def getGvalue(self):
        return self.Gvalue

    def setParent(self,p):
        self.parent = p

    def getParent(self):
        return self.parent
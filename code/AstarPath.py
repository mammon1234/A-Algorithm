import cell
import math
import heapq

class AstarPath(object):
    def __init__(self,MATRIX,STARTROW, STARTCOLUMN, ENDROW, ENDCOLUMN,weight,htype):
        #Return a grid object with initial values.
        self.MATRIX= MATRIX
        self.STARTROW=STARTROW
        self.STARTCOLUMN=STARTCOLUMN
        self.ENDROW=ENDROW
        self.ENDCOLUMN=ENDCOLUMN
        self.weight =weight
        self.htype =htype
        self.path=set()
        self.visited=set()

        for row in range(120):
            for column in range(160):
                self.MATRIX[row][column].setFvalue(float('inf'))
                self.MATRIX[row][column].setGvalue(float('inf'))
                self.MATRIX[row][column].setHvalue(float('inf'))
                self.MATRIX[row][column].setParent((row,column))

    def computeHvalue(self, row, column):
            #manhandun distance
        if (self.htype == '1'):
            return 0.25*(abs(row - self.ENDROW) + abs(column - self.ENDCOLUMN))
        if (self.htype == '2'):
            #octile distance
            return (math.sqrt(2) - 1) * min(abs(row - self.ENDROW), abs(column - self.ENDCOLUMN)) + max(abs(row - self.ENDROW), abs(column - self.ENDCOLUMN))
        if (self.htype == '3'):
            #Euclidean distance
            return math.sqrt(math.pow(abs(row - self.ENDROW),2)+math.pow(abs(column - self.ENDCOLUMN),2))
        if (self.htype == '4'):
            #square distance
            return math.pow(abs(row - self.ENDROW),2)+math.pow(abs(column - self.ENDCOLUMN),2)
        if (self.htype == '5'):
            # self defined
            return (math.sqrt(3)-1)*min(abs(row - self.ENDROW),abs(column - self.ENDCOLUMN))+max(abs(row - self.ENDROW),abs(column - self.ENDCOLUMN))

    def setPath(self):
        curRow=self.ENDROW
        curColumn=self.ENDCOLUMN
        while(curRow,curColumn)!=self.MATRIX[curRow][curColumn].getParent():
            #print str(curRow)+"[]"+str(curColumn)
            self.path.add((curRow,curColumn))
            (curRow,curColumn) = self.MATRIX[curRow][curColumn].getParent()

    def updateCell(self,currow,curcolumn,sourcerow,sourcecolumn):
        hvalue = self.computeHvalue(currow,curcolumn)
        self.MATRIX[currow][curcolumn].setHvalue(hvalue)
        cur_state = self.MATRIX[currow][curcolumn].getState()
        source_state = self.MATRIX[sourcerow][sourcecolumn].getState()
        cost=0
        if(currow ==sourcerow or curcolumn == sourcecolumn):
            if(cur_state == 'a' or cur_state == 'b') and (source_state == 'a' or source_state == 'b'):
                if(cur_state =='a'):
                    cur_state = 1
                elif(cur_state == 'b'):
                    cur_state = 2
                if(source_state == 'a'):
                    source_state =1
                elif(source_state == 'b'):
                    source_state =2
                cost=(cur_state+source_state)/8.0
            else:
                if(cur_state =='a'):
                    cur_state = 1
                elif(cur_state == 'b'):
                    cur_state = 2
                if(source_state == 'a'):
                    source_state =1
                elif(source_state == 'b'):
                    source_state =2
                cost=(cur_state+source_state)/2.0
        else:
            if (cur_state == 'a'):
                cur_state = 1
            elif (cur_state == 'b'):
                cur_state = 2
            if (source_state == 'a'):
                source_state = 1
            elif (source_state == 'b'):
                source_state = 2
            cost = (cur_state + source_state)*math.sqrt(2)/ 2.0

        gvalue = cost+self.MATRIX[sourcerow][sourcecolumn].getGvalue()

        if gvalue < self.MATRIX[currow][curcolumn].getGvalue():
            self.MATRIX[currow][curcolumn].setGvalue(gvalue)
            self.MATRIX[currow][curcolumn].setFvalue(gvalue+hvalue*float(self.weight))
            self.MATRIX[currow][curcolumn].setParent((sourcerow,sourcecolumn))
            return gvalue+hvalue*float(self.weight)
        else:
            return self.MATRIX[currow][curcolumn].getGvalue()+hvalue*float(self.weight)


    def finding(self):
        find_bool =0
        Gvalue =0
        Hvalue =self.computeHvalue(self.STARTROW, self.STARTCOLUMN)
        Fvalue =Gvalue+Hvalue*float(self.weight)
        self.path.clear()
        self.visited.clear()

        self.MATRIX[self.STARTROW][self.STARTCOLUMN].setParent((self.STARTROW,self.STARTCOLUMN))
        self.MATRIX[self.STARTROW][self.STARTCOLUMN].setGvalue(0)
        self.MATRIX[self.STARTROW][self.STARTCOLUMN].setHvalue(Hvalue)
        self.MATRIX[self.STARTROW][self.STARTCOLUMN].setFvalue(Fvalue)

        fringe = PriorityQueue()
        fringe.put((self.STARTROW,self.STARTCOLUMN),Fvalue)
        closed=set()
        neighbour = set()
        self.visited.add((self.STARTROW, self.STARTCOLUMN))
        while(not fringe.empty()):
            #Fvalue = fringe.get_smallest()
            (curRow,curColumn)=fringe.get()
            if(curRow,curColumn) ==(self.ENDROW,self.ENDCOLUMN):
                find_bool=1
                break
            if(curRow,curColumn) in closed:
                continue
            #print Fvalue
            #print str(curRow)+"[]"+str(curColumn)+"parent :"+str(self.MATRIX[curRow][curColumn].getParent())
            closed.add((curRow,curColumn))

            for i in range(curRow-1,curRow+2):
                for j in range(curColumn-1,curColumn+2):
                    if(i>=0 and i<=119 and j>=0 and j <= 159):
                        if((i,j) not in closed):
                            neighbour.add((i,j))
            for k in neighbour:
                self.visited.add((k[0],k[1]))
                if(self.MATRIX[k[0]][k[1]].isBlocked() or (k[0],k[1]) in closed):
                    continue
                else:
                    Fvalue=self.updateCell(k[0],k[1],curRow,curColumn)
                    fringe.put((k[0],k[1]),Fvalue)
                    #print Fvalue
            neighbour.clear()
        #print "path path"

        if(find_bool == 1):
            self.setPath()
            print "path :"+str(len(self.path))
            print "path find"
        else:
            print "no path"

        print "visited :"+str(len(self.visited))

        return (self.MATRIX,self.path,len(self.path),len(self.visited))

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

    def get_smallest(self):
        return self.elements[0][0]

    def replace(self, item, priority):
        length = len(self.elements)
        boolis = 0
        for i in range(length):
            if (self.elements[i][1] == item):
                boolis = 1
                self.elements[i] = self.elements[0]
        if(boolis == 1):
            heapq.heappop(self.elements)
        heapq.heappush(self.elements, (priority, item))







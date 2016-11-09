import cell
import math
import heapq

class SequentialAstar(object):
    def __init__(self,MATRIX,STARTROW, STARTCOLUMN, ENDROW, ENDCOLUMN,weight1,weight2):
        #Return a grid object with initial values.
        self.MATRIX= MATRIX
        self.STARTROW=STARTROW
        self.STARTCOLUMN=STARTCOLUMN
        self.ENDROW=ENDROW
        self.ENDCOLUMN=ENDCOLUMN
        self.weight1 =weight1
        self.weight2 =weight2
#        self.htype =htype
        self.path=set()
        self.visited=set()

        for row in range(120):
            for column in range(160):
                self.MATRIX[row][column].setFvalue(float('inf'))
                self.MATRIX[row][column].setGvalue(float('inf'))
                self.MATRIX[row][column].setHvalue(float('inf'))
                self.MATRIX[row][column].setParent((row,column))


    def computeHvalue(self, row, column,htype):
            #manhandun distance
        if (htype == 0):
            return 0.25*(abs(row - self.ENDROW) + abs(column - self.ENDCOLUMN))
        if (htype == 1):
            #octile distance
            return (math.sqrt(2) - 1) * min(abs(row - self.ENDROW), abs(column - self.ENDCOLUMN)) + max(abs(row - self.ENDROW), abs(column - self.ENDCOLUMN))
        if (htype == 2):
            #Euclidean distance
            return math.sqrt(math.pow(abs(row - self.ENDROW),2)+math.pow(abs(column - self.ENDCOLUMN),2))
        if (htype == 3):
            #square distance
            return math.pow(abs(row - self.ENDROW),2)+math.pow(abs(column - self.ENDCOLUMN),2)
        if (htype == 4):
            # self defined
            return (math.sqrt(3)-1)*min(abs(row - self.ENDROW),abs(column - self.ENDCOLUMN))+max(abs(row - self.ENDROW),abs(column - self.ENDCOLUMN))

    def setPath(self,MATRIX):
        names= locals()
        curRow=self.ENDROW
        curColumn=self.ENDCOLUMN
        while(curRow,curColumn)!=MATRIX[curRow][curColumn].getParent():
            #print str(curRow)+"[]"+str(curColumn)
            self.path.add((curRow,curColumn))
            (curRow,curColumn) = MATRIX[curRow][curColumn].getParent()

    def updateCell(self,currow,curcolumn,sourcerow,sourcecolumn,MATRIX,i):
        names= locals()
        hvalue = self.computeHvalue(currow,curcolumn,i)
        MATRIX[currow][curcolumn].setHvalue(hvalue)
        cur_state = MATRIX[currow][curcolumn].getState()
        source_state = MATRIX[sourcerow][sourcecolumn].getState()
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

        gvalue = cost+MATRIX[sourcerow][sourcecolumn].getGvalue()

        if gvalue < MATRIX[currow][curcolumn].getGvalue():
            MATRIX[currow][curcolumn].setGvalue(gvalue)
            MATRIX[currow][curcolumn].setFvalue(gvalue+hvalue*float(self.weight1))
            MATRIX[currow][curcolumn].setParent((sourcerow,sourcecolumn))
            return (MATRIX,gvalue+hvalue*float(self.weight1))
        else:
            return (MATRIX,MATRIX[currow][curcolumn].getGvalue()+hvalue*float(self.weight1))


    def finding(self):

        names = locals()
        find_bool =5

        self.path.clear()
        self.visited.clear()
        MATRIX0=self.MATRIX
        MATRIX1=self.MATRIX
        MATRIX2=self.MATRIX
        MATRIX3=self.MATRIX
        MATRIX4=self.MATRIX
        for ith in range(5):
            Hvalue = self.computeHvalue(self.STARTROW, self.STARTCOLUMN,ith)
            #print "Hvalue :"+str(Hvalue)
            #print self.weight1
            Fvalue = 0 + Hvalue * float(self.weight1)
            locals()['MATRIX' + str(ith)][self.STARTROW][self.STARTCOLUMN].setParent((self.STARTROW,self.STARTCOLUMN))
            locals()['MATRIX' + str(ith)][self.STARTROW][self.STARTCOLUMN].setGvalue(0)
            locals()['MATRIX' + str(ith)][self.STARTROW][self.STARTCOLUMN].setHvalue(Hvalue)
            locals()['MATRIX' + str(ith)][self.STARTROW][self.STARTCOLUMN].setFvalue(Fvalue)
            locals()['fringe' + str(ith)] = PriorityQueue()
            locals()['fringe' + str(ith)].put((self.STARTROW,self.STARTCOLUMN),Fvalue)
            locals()['closed' + str(ith)]=set()
        neighbour = set()
        self.visited.add((self.STARTROW, self.STARTCOLUMN))
        flag =1
        while (locals()['fringe' + str(0)].get_smallest()!= float("inf")):
            for ith in range(1,5):
                F0value = locals()['fringe' + str(0)].get_smallest()
                if (ith != flag):
                    ith = flag
                if(locals()['fringe' + str(ith)].get_smallest() <= float(self.weight2) * F0value):
                    Givalue = locals()['MATRIX' + str(ith)][self.ENDROW][self.ENDCOLUMN].getGvalue()
                    if(Givalue <= locals()['fringe' + str(ith)].get_smallest()):
                        if( Givalue != float("inf")):
                            find_bool = ith
                            break
                            # finish
                    else:
                        (curRow, curColumn) = locals()['fringe' + str(ith)].get()
                        if(curRow,curColumn) in locals()['closed' + str(ith)]:
                            continue
                        else:
                            flag = flag+1
                            if(flag == 5):
                                flag =1
                            locals()['closed' + str(ith)].add((curRow,curColumn))
                            for i in range(curRow - 1, curRow + 2):
                                for j in range(curColumn - 1, curColumn + 2):
                                    if (i >= 0 and i <= 119 and j >= 0 and j <= 159):
                                        if ((i, j) not in locals()['closed' + str(ith)]):
                                            neighbour.add((i, j))
                            for k in neighbour:
                                self.visited.add((k[0], k[1]))
                                if (locals()['MATRIX' + str(ith)][k[0]][k[1]].isBlocked() or (k[0], k[1]) in locals()['closed' + str(ith)]):
                                    continue
                                else:
                                    (locals()['MATRIX' + str(ith)],Fvalue) = self.updateCell(k[0], k[1], curRow, curColumn,names['MATRIX%s' % ith],ith)
                                    locals()['fringe' + str(ith)].put((k[0], k[1]), Fvalue)
                                    # print Fvalue
                            neighbour.clear()
                else:
                    Givalue = locals()['MATRIX' + str(0)][self.ENDROW][self.ENDCOLUMN].getGvalue()
                    if(Givalue <= locals()['fringe' + str(0)].get_smallest()):
                        if( Givalue != float("inf")):
                            find_bool = 0
                            break
                    else:
                        (curRow, curColumn) = locals()['fringe' + str(0)].get()
                        if(curRow,curColumn) in locals()['closed' + str(0)]:
                            continue
                        else:
                            locals()['closed' + str(0)].add((curRow, curColumn))
                            for i in range(curRow - 1, curRow + 2):
                                for j in range(curColumn - 1, curColumn + 2):
                                    if (i >= 0 and i <= 119 and j >= 0 and j <= 159):
                                        if ((i, j) not in locals()['closed' + str(0)]):
                                            neighbour.add((i, j))
                            for k in neighbour:
                                self.visited.add((k[0], k[1]))
                                if (locals()['MATRIX' + str(0)][k[0]][k[1]].isBlocked() or (k[0], k[1]) in locals()['closed' + str(0)]):
                                    continue
                                else:
                                    (MATRIX0,Fvalue) = self.updateCell(k[0], k[1], curRow, curColumn, MATRIX0,0)
                                    locals()['fringe' + str(0)].put((k[0], k[1]), Fvalue)
                                     # print Fvalue
                        neighbour.clear()

            if(find_bool != 5):
                break
        print "visited :"+str(len(self.visited))
        if(find_bool != 5):
            self.setPath(locals()['MATRIX' + str(find_bool)])
            print "path :"+str(len(self.path))
            print "path find"
            return (locals()['MATRIX' + str(find_bool)], self.path, len(self.path), len(self.visited))

        else:
            print "no path"
            return (MATRIX0, self.path, len(self.path), len(self.visited))


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







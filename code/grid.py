import cell
import pygame
import random


class grid(object):
    def __init__(self,rows,columns, width, height, margin):
        #Return a grid object with initial values.

        self.Matrix = []
        for row in range(rows):
            # Add an empty array that will hold each cell in this row
            self.Matrix.append([])
            for column in range(columns):
                # Append a cell
                self.Matrix[row].append(cell.cell(row, column))

        self.rows = rows
        self.columns = columns
        self.width = width
        self.height = height
        self.margin = margin

    def getCell(self, r, c):
        #Return a cell object from row r and column c
        return self.Matrix[r][c].getState()

    def printGrid(self):
        #Prints grid in a window using pygame

        # Define some colors
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        GREY = (50, 50, 50)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)
        BLUE = (0, 0, 255)
        YELLOW = (255, 255, 0)

        # This sets the WIDTH and HEIGHT of each grid location
        WIDTH = self.width
        HEIGHT = self.height
        # This sets the margin between each cell
        MARGIN = self.margin

        # List to hold the traveled path
        travPath = []

        GRID_rows = self.rows
        GRID_columns = self.columns
        # Create a 2 dimensional array. A two dimensional
        # array is simply a list of lists.
        grid = []
        f = open('map.txt', 'a+')
        for row in range(GRID_rows):
            # Add an empty array that will hold each cell
            # in this row
            grid.append([])
            for column in range(GRID_columns):
                grid[row].append(self.Matrix[row][column].getState())  # Append a cell
                if(self.Matrix[row][column].getHighWayIndex() != 0):
                    f.write(str(grid[row][column])+str(self.Matrix[row][column].getHighWayIndex()))
                    if(column !=159):
                        f.write(",")
                else:
                    f.write(str(grid[row][column]))
                    if(column !=159):
                        f.write(",")
            f.write("\r\n")
        f.close()

        # Loop until the user clicks the close button.
        done = False

        # Initialize pygame
        pygame.init()

        # Set the HEIGHT and WIDTH of the screen
        WINDOW_SIZE = [GRID_columns * (WIDTH + MARGIN), GRID_rows* (HEIGHT + MARGIN)]
        screen = pygame.display.set_mode(WINDOW_SIZE)

        # Display Title
        pygame.display.set_caption("Map")

        # -------- Main Program Loop -----------
        while not done:
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop

            screen.fill(BLACK)

            # Draw the grid
            for row in range(GRID_rows):
                for column in range(GRID_columns):
                    if grid[row][column] == 1:
                        color = WHITE
                    if grid[row][column] == 2:
                        color = YELLOW
                    if grid[row][column] == 0:
                        color = BLACK
                    if grid[row][column] == 'a' or grid[row][column] == 'b':
                        color = BLUE
                    pygame.draw.rect(screen,
                                     color,
                                     [(MARGIN + WIDTH) * column ,
                                      (MARGIN + HEIGHT) * row,
                                      WIDTH,
                                      HEIGHT])

            pygame.display.flip()
        # on exit.
        pygame.quit()

    def generate(self):
        #Generates the hardcenter
        hardcenter = set()
        i=0
        while (i < 8):
            xrand = random.randint(15,104)
            yrand = random.randint(15,144)
            if((xrand,yrand) not in hardcenter):
                hardcenter.add((xrand,yrand))
                i=i+1
        for k in hardcenter:
            for row in range(k[0]-15,k[0]+16):
                for column in range(k[1]-15,k[1]+16):
                    if (not self.Matrix[row][column].isHard()):
                        if (random.randint(0, 99) >= 50):
                            self.Matrix[row][column].setHard()
                            #print row,column
        print "hard_center_success"

        #gennerate the 4 highway
        ways = 4
        path = set()
        while (ways > 0):
            pathcross = 0
            HighWayStartPoint = random.randint(0,556)
            #direction up:1, down:2, left:3, right:4
            if(HighWayStartPoint == 0 or HighWayStartPoint ==159 or HighWayStartPoint == 278 or HighWayStartPoint == 437):
                pathcross =1
            elif( HighWayStartPoint <160):
                highwayRow = 0
                highwayColumn = HighWayStartPoint
                direction = 2
            elif(HighWayStartPoint <279):
                highwayColumn = 159
                highwayRow = HighWayStartPoint-159
                direction = 3
            elif(HighWayStartPoint <438):
                highwayRow = 119
                highwayColumn = 159+(278 - HighWayStartPoint)
                direction = 1
            else:
                highwayColumn=0
                highwayRow = 119+(437-HighWayStartPoint)
                direction = 4
            #print "HighWayStartPoint"+"("+str(highwayRow)+","+str(highwayColumn)+")"

            cellCount =20
            boundaryflag = 0
            path.clear()

            while(highwayRow<=119 and highwayRow >=0 and highwayColumn>=0 and highwayColumn<=150 and pathcross == 0):


                cellCount=cellCount-1

                #print "generate highway"
                if(self.Matrix[highwayRow][highwayColumn].isHighway() or ((highwayRow,highwayColumn) in path)):
                    pathcross = 1
                    #print "path cross"
                    break
                path.add((highwayRow,highwayColumn))
                #if((highwayRow,highwayColumn) in path):
                #    print str(highwayRow)+"[]"+str(highwayColumn)

                if(highwayRow ==0 or highwayRow ==119 or highwayColumn == 0 or highwayColumn ==159):
                    if(boundaryflag == 1):
                        boundaryflag =2
                        #print "meet the boundary"
                        break
                if(boundaryflag ==0):
                    boundaryflag = 1

                if(cellCount > 0):
                    if(direction == 1):
                        highwayRow=highwayRow-1
                    if(direction == 2):
                        highwayRow=highwayRow+1
                    if(direction == 3):
                        highwayColumn = highwayColumn-1
                    if(direction == 4):
                        highwayColumn = highwayColumn +1
                else:
                    cellCount =20
                    newDirect = random.random()
                    #print newDirect
                    if(newDirect < 0.6):
                        #print newDirect+1
                        if (direction == 1):
                            highwayRow = highwayRow - 1
                        if (direction == 2):
                            highwayRow = highwayRow + 1
                        if (direction == 3):
                            highwayColumn = highwayColumn - 1
                        if (direction == 4):
                            highwayColumn = highwayColumn + 1
                    if(newDirect < 0.8 and newDirect >= 0.6):
                        #print newDirect+2
                        if (direction == 1):
                            direction = 3
                            highwayColumn = highwayColumn - 1
                        elif (direction == 2):
                            direction = 3
                            highwayColumn = highwayColumn - 1
                        elif (direction == 3):
                            direction = 1
                            highwayRow = highwayRow - 1
                        elif (direction == 4):
                            direction = 1
                            highwayRow = highwayRow - 1
                    if (newDirect >= 0.8):
                        #print newDirect+3
                        if (direction == 1):
                            direction = 4
                            highwayColumn = highwayColumn + 1
                        elif (direction == 2):
                            direction = 4
                            highwayColumn = highwayColumn + 1
                        elif (direction == 3):
                            direction = 2
                            highwayRow = highwayRow + 1
                        elif (direction == 4):
                            direction = 2
                            highwayRow = highwayRow + 1

            if((pathcross == 0) and(len(path)>99) and boundaryflag ==2):
                print "one highway build"
                print (len(path))
                for cell in path:
                    #print str(cell[0])+"[]"+str(cell[1])
                    self.Matrix[cell[0]][cell[1]].setHighway(ways)
                #print ways
                ways=ways-1

        #generate Blocked cell
        blocknum=3840
        while(blocknum >0):
            blockrow = random.randint(0,119)
            blockcolumn = random.randint(0,159)
            if(not(self.Matrix[blockrow][blockcolumn].isBlocked() or self.Matrix[blockrow][blockcolumn].isHighway())):
                self.Matrix[blockrow][blockcolumn].setBlocked()
                blocknum=blocknum-1

        #generate the start point and end point
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
        #save file
        f = open('map.txt', 'w+')
        f.write(str(startRow)+","+str(startColumn)+"\r\n")
        f.write(str(endRow) + "," + str(endColumn) + "\r\n")
        for k in hardcenter:
            f.write(str(k[0]) + "," + str(k[1]) + "\r\n")
        f.write(str(120)+","+str(160)+"\r\n")
        f.close();




    def generateRowPoint(self):
        point = random.randint(0, 40)
        if(point >= 20):
            point = 119 +(20 - point)
        return point


    def generateColumnPoint(self):
        point = random.randint(0, 40)
        if (point >= 20):
            point = 159 + (20 - point)
        return point




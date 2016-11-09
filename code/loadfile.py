import cell
import pygame

class loadfile(object):
    def __init__(self):
        try:
            f=open('map.txt','r')
        except IOError:
            print "file don't exist, please check!"
        Alllines = f.readlines()
        count = 0
        self.hardcenter = set()
        self.Matrix = []
        self.path=set()
        WIDTH = 4
        HEIGHT =4
        MARGIN =1
        ROWS=0
        COLUMNS =0

        for i in range(120):
            self.Matrix.append([])
        for eachline in Alllines:
            count=count+1
            line = eachline.split(',')
            if count == 1:
                self.startRow = int(line[0])
                self.startColumn = int(line[1])
            if count == 2:
                self.endRow =int(line[0])
                self.endColumn = int(line[1])
            if count<=10 and count >=3:
                self.hardcenter.add((int(line[0]),int(line[1])))
            if count == 11:
                self.ROWS=int(line[0])
                self.COLUMNS=int(line[1])
            if count>=12 and count<=131:
                #print count
                for i in range(160):
                    self.Matrix[count-12].append(cell.cell(count-12, i))
                    if(i!=159):
                        if((line[i] == '0') or (line[i] == '1') or (line[i] =='2')):
                            self.Matrix[count - 12][i].setState(int(line[i]))
                        else:
                            self.Matrix[count - 12][i].setState(line[i][0])
                            self.Matrix[count - 12][i].setHighway(int(line[i][1]))
                    else:
                        if((line[i][0] == '0') or (line[i][0] == '1') or (line[i][0] =='2')):
                            self.Matrix[count - 12][i].setState(int(line[i][0]))
                        else:
                            self.Matrix[count - 12][i].setState(line[i][0])
                            self.Matrix[count - 12][i].setHighway(int(line[i][1]))
        self.path.add((self.startRow , self.startColumn))
        self.path.add((self.endRow, self.endColumn))
        f.close()

    def getValue(self):
        return (self.Matrix, self.startRow, self.startColumn,self.endRow,self.endColumn,self.hardcenter)

    def printM(self):
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        GREY = (50, 50, 50)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)
        BLUE = (0, 0, 255)
        YELLOW = (255, 255, 0)
        color =BLACK

        # Loop until the user clicks the close button.
        done = False

        # Initialize pygame
        pygame.init()

        # Set the HEIGHT and WIDTH of the screen
        WINDOW_SIZE = [self.COLUMNS * (4 + 1), self.ROWS * (4 + 1)]
        screen = pygame.display.set_mode(WINDOW_SIZE)

        # Display Title
        pygame.display.set_caption("Map")
        # -------- Main Program Loop -----------
        while not done:
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop

            screen.fill(BLACK)

            for row in range(self.ROWS):
                for column in range(self.COLUMNS):
                    if self.Matrix[row][column].getState() == 1:
                        color = WHITE
                    if self.Matrix[row][column].getState() == 2:
                        color = YELLOW
                    if self.Matrix[row][column].getState() == 0:
                        color = BLACK
                    if self.Matrix[row][column].getState() == 'a' or self.Matrix[row][column].getState() == 'b':
                        color = BLUE
                    if (row,column) in self.path:
                        color = RED
                    pygame.draw.rect(screen, color, [(1 + 4) * column, (1 + 4) * row, 4, 4])

            pygame.display.flip()
        # on exit.
        pygame.quit()


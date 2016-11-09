import cell
import pygame

class printMap(object):
    def __init__(self,MATRIX,path):
        self.Matrix = MATRIX
        self.path =path
        self.ROWS=120
        self.COLUMNS=160

    def printM(self):
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        GREY = (50, 50, 50)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)
        BLUE = (0, 0, 255)
        YELLOW = (255, 255, 0)

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

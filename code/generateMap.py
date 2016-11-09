import grid
import pickle
class generateMap(object):
    def __init__(self):
        g = grid.grid(120,160,4,4,1)
        g.generate()
#f = open('120x160Map', 'w+')
#pickle.dump(g,f)
#f.close()
        g.printGrid()
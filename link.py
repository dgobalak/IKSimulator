from coordinate import Coordinate
import numpy as np

class Link:
    ORIGIN = np.array((0, 0))
    
    def __init__(self, link_num, length, parent=None):
        self.link_num = link_num
        self.length = length
        self.parent = parent
                
        if link_num == 0:
            self.start = Coordinate(0, 0)
            self.end = Coordinate(0, self.length)
        else:
            self.start = self.parent.end
            self.end =  Coordinate(*(self.parent.end.get_coordinate() + np.array((0, length))))   
    
    def move(self, x2, y2):
        a = self.start.get_coordinate() # starting coordinate
        b = self.end.get_coordinate() # ending coordinate
        c = np.array((x2, y2)) # target coordinate
        
        u_hat = (c - a) / np.linalg.norm(c - a) # target unit vector
        new_start = c - (u_hat * self.length)
        new_end = c
        
        self.start.set(*new_start)
        self.end.set(*new_end)

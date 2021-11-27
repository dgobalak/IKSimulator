from coordinate import Coordinate
import numpy as np

class Link:
    ORIGIN = np.array((0, 0))
    def __init__(self, link_num, length):
        self.link_num = link_num
        self.length = length
        self.start = Coordinate(0, link_num)
        self.end = Coordinate(0, (link_num+1)*self.length)
    
    def move(self, x2, y2):
        a = self.start.get_coordinate() # starting coordinate
        b = self.end.get_coordinate() # ending coordinate
        c = np.array((x2, y2)) # target coordinate
        
        u_hat = (c - a) / np.linalg.norm(c-a) # target unit vector
        new_start = c - (u_hat * self.length)
        new_end = c
        
        self.start.set(*new_start)
        self.end.set(*new_end)

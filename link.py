from coordinate import Coordinate

class Link:
    ORIGIN = (0, 0)
    def __init__(self, link_num, length):
        self.link_num = link_num
        self.length = length
        self.start = Coordinate(*self.ORIGIN)
        self.end = Coordinate(*self.ORIGIN)
    

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x
    
    def set_y(self, y):
        self.y = y
    
    def set(self, x, y):
        self.set_x(x)
        self.set_y(y)
        return self
    
    def get_coordinate(self):
        return (self.x, self.y)
    
    def __str__(self):
        return f'(x: {self.x}, y: {self.y})'

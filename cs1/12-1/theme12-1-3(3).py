import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        return math.sqrt(new_x ** 2 + new_y ** 2)


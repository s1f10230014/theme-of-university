class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h
        print(self.width)

    def area(self):
        return self.width * self.height

r = Rectangle(5, 4)
r.width
r.height
r.area()
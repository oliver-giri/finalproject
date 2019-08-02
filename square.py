from rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, x, y, color, sideLength):
        super().__init__(x, y, color, sideLength, sideLength)

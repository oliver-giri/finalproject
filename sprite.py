from square import Square

class Sprite(Square):

    def __init__(self, x, y, color, sideLength, xVelocity, yVelocity):
        super().__init__(x, y, color, sideLength)
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity

    def move(self):
        self.x += self.xVelocity
        self.y += self.yVelocity
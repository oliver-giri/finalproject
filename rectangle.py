import pygame

class Rectangle():

    def __init__(self, x, y, color, width, height):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def getRect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)



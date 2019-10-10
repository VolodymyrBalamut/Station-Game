import pygame
from figures import *

class Drawable:
    def draw(self):
        pass

class Ticket(Drawable):
    def __init__(self, name, display, color, x, y):
        self.name = name
        self.display = display
        self.color = color
        self.x = x
        self.y = y
        self.body = [
                    Rectangle(display, color, x, y),
                    Rectangle(display, color, x+100, y)
                     ]
    def draw(self):
        for part in self.body:
            part.draw()

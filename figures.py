import pygame

class Figure:
    def __init__(self, display, color, x, y):
        self.display = display
        self.color = color
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
    def draw(self):
        pass

class Circle(Figure):
    def __init__(self, display, color, x, y):
        super().__init__(display, color, x, y)
    def draw(self):
        pygame.draw.circle(self.display,self.color,(self.x+int(self.width/2), self.y+int(self.height/2)), int(self.width/2), 3)

class Line(Figure):
    def __init__(self, display, color, startPoint, endPoint):
        super().__init__(display, color, startPoint, endPoint)
        self.startPoint = startPoint
        self.endPoint = endPoint
    def draw(self):
        pygame.draw.line(self.display,self.color, self.startPoint, self.endPoint, 3)

class Rectangle(Figure):
    def __init__(self, display, color, x, y):
        super().__init__(display, color, x, y)
        self.rect = (x, y, self.width, self.height)
    def draw(self):
        pygame.draw.rect(self.display,self.color,self.rect,3)

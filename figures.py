import pygame

class Figure:
    def __init__(self, display, color, x, y, width = 50, height = 135):
        self.display = display
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def draw(self):
        pass

class Circle(Figure):
    def __init__(self, display, color, x, y, width = 50, height = 135):
        super().__init__(display, color, x, y, width, height)
    def draw(self):
        pygame.draw.circle(self.display,self.color,(self.x+int(self.width/2), self.y+int(self.height/2)), int(self.height), 3)

class Line(Figure):
    def __init__(self, display, color, startPoint, endPoint):
        super().__init__(display, color, startPoint, endPoint)
        self.startPoint = startPoint
        self.endPoint = endPoint
    def draw(self):
        pygame.draw.line(self.display,self.color, self.startPoint, self.endPoint, 3)

class Rectangle(Figure):
    def __init__(self, display, color, x, y, width = 50, height =50):
        super().__init__(display, color, x, y, width, height)
        self.rect = (x, y, self.width, self.height)
    def draw(self):
        pygame.draw.rect(self.display,self.color,self.rect, 3)

class Text(Figure):
    def __init__(self, display, color, x, y, msg):
        super().__init__(display, color, x, y)
        self.font = pygame.font.SysFont(None, 25)
        self.msg = msg
    def draw(self):
        screen_text = self.font.render(self.msg, True, self.color)
        self.display.blit(screen_text, [self.x, self.y])

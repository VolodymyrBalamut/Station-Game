import pygame


class Figure:
    def __init__(self, display, color, x = 0, y = 0, width = 50, height = 135):
        self.__display = display
        self.__color = color
        self.__x = x if isinstance(x, int) else 0
        self.__y = y if isinstance(x, int) else 0
        self.__width = width if isinstance(width, int) else 50
        self.__height = height if isinstance(height, int) else 135
    def draw(self):
        pass
    def get_display(self):
        return self.__display
    def get_color(self):
        return self.__color  
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    def get_width(self):
        return self.__width
    def get_height(self):
        return self.__height


class Circle(Figure):
    def __init__(self, display, color, x, y, width = 50, height = 135):
        super().__init__(display, color, x, y, width, height)
    def draw(self):
        pygame.draw.circle(self.get_display(), self.get_color(), (self.get_x() + int(self.get_width()/2), self.get_y()+int(self.get_height()/2)), int(self.get_height()), 3)

class Line(Figure):
    def __init__(self, display, color, startPoint, endPoint):
        super().__init__(display, color, startPoint, endPoint)
        self.__startPoint = startPoint
        self.__endPoint = endPoint
    def draw(self):
        pygame.draw.line(self.get_display(), self.get_color(), self.__startPoint, self.__endPoint, 3)

class Rectangle(Figure):
    def __init__(self, display, color, x, y, width = 50, height =50):
        super().__init__(display, color, x, y, width, height)
        self.__rect = (x, y, width, height)
    def draw(self):
        pygame.draw.rect(self.__display,self.__color,self.__rect, 3)

class Text(Figure):
    def __init__(self, display, color, x, y, msg, font_size = 25):
        super().__init__(display, color, x, y)
        self.font = pygame.font.SysFont(None, font_size)
        self.msg = msg
    def draw(self):
        screen_text = self.font.render(self.msg, True, self.__color)
        self.__display.blit(screen_text, [self.__x, self.__y])

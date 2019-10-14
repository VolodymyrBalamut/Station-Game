from colors import colors
from abc import ABC, abstractmethod
import pygame

class Drawable(ABC):
    def __init__(self, display, surface, name="Drawable", color=colors["BLACK"], x=0, y=0, width = 25, height = 80):
        self.__display = display
        self.__surface = surface
        self.__name = name
        self.__color = color if isinstance(colors["BLACK"], tuple) else colors["BLACK"]
        self.__x = x if isinstance(x, int) else 0
        self.__y = y if isinstance(x, int) else 0
        self.__width = width if isinstance(width, int) else 25
        self.__height = height if isinstance(height, int) else 80
    def draw(self):
        pass
    def current_pos(self):
        return str("( X= " + str(self.__x) + ", Y = " + str(self.__y) + " )") 
    def get_display(self):
        return self.__display
    def get_surface(self):
        return self.__surface
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_color(self, color):
        self.__color = color
    def get_color(self):
        return self.__color  
    def set_x(self, x):
        if (isinstance(x, int)):
            self.__x = x
            self.__check_border()
    def move_x(self, x):
        if (isinstance(x, int)):
            self.__x += x
            self.__check_border()
    def get_x(self):
        return self.__x
    def set_y(self, y):
        if (isinstance(y, int)):
            self.__y = y
            self.__check_border()
    def move_y(self, y):
        if (isinstance(y, int)):
            self.__y += y
            self.__check_border
    def get_y(self):
        return self.__y
    def __check_border(self):
        w, h = self.__surface.get_size()
        if(self.get_x() > w):
            self.set_x(0)
        if(self.get_x() < 0):
            self.set_x(w - 20)
        if(self.get_y() > h):
            self.set_y(0)
        if(self.get_y() < 0):
            self.set_y(h - 100)
    def get_width(self):
        return self.__width
    def get_height(self):
        return self.__height


class Person(Drawable):
    def __init__(self, display, surface, name="John", color=colors["BLACK"], x=0, y=0):
        super().__init__(display, surface, name, color, x, y)
        self.name = "Person " + name
        self.body = self.makeBody()
    def myfunc(self):
        print("Hello my name is " + self.name)
    def makeBody(self):
        part_size = int(self.get_height() / 8)
        return [
                 Circle(self.get_display(), self.get_surface(), "", self.get_color(), self.get_x(), self.get_y(), self.get_width(), part_size),
                 Line(self.get_display(), self.get_surface(), "", self.get_color(), (self.get_x()+int(self.get_width() / 2), self.get_y()+part_size), (self.get_x()+ int(self.get_width() / 2), self.get_y() + 5*part_size)),
                 Line(self.get_display(), self.get_surface(),"", self.get_color(), (self.get_x(), self.get_y()+3*part_size), (self.get_x()+self.get_width(), self.get_y()+3*part_size)),
                 Line(self.get_display(), self.get_surface(),"", self.get_color(), (self.get_x()+int(self.get_width() / 2), self.get_y()+5*part_size), (self.get_x(), self.get_y()+self.get_height())),
                 Line(self.get_display(), self.get_surface(),"", self.get_color(), (self.get_x()+int(self.get_width() / 2), self.get_y()+5*part_size), (self.get_x()+self.get_width(), self.get_y()+self.get_height())),
                 Text(self.get_display(), self.get_surface(), self.name, self.get_color(), self.get_x(), self.get_y()+self.get_height() +10)
                ]
    def draw(self):
        for part in self.body:
            part.draw()
    def changePosition(self, step_x, step_y):
        self.move_x(step_x if isinstance(step_x, int) else 0)
        self.move_y(step_y if isinstance(step_y, int) else 0)
        self.body = self.makeBody()

class Passenger(Person):
    def __init__(self, display, surface, name="John", color=colors["BLACK"], x=0, y=0):
        super().__init__(display, surface, name, color, x, y)
        self.name = "Passenger " + name
    
class Ticket(Drawable):
    def __init__(self, display, surface, name="Ticket", color=colors["BLACK"], x=0, y=0, width = 10, height = 10):
        super().__init__(display, surface,  name, color, x, y, width, height)
        self.body = self.makeBody()
        self.__ticket_count = 0
    def makeBody(self):
        return [
                 Rectangle(self.get_display(), self.get_surface(), "", self.get_color(), self.get_x(), self.get_y(), self.get_width(), self.get_height()),
                 Text(self.get_display(), self.get_surface(), self.get_name(), self.get_color(), self.get_x(), self.get_y() +self.get_height() + 10)
                ]
    def change_name(self, name):
        self.set_name(name)
        self.body = self.makeBody()
    def draw(self):
        for part in self.body:
            part.draw()
    def ticket_inc(self):
        self.__ticket_count += 1
        self.change_name("Tickets " + str(self.get_ticket_count()))
    def get_ticket_count(self):
        return self.__ticket_count
    def buy(self):
        self.ticket_inc()
        return "You have bought new ticket! You have " + str(self.get_ticket_count()) + " tickets"

class CashRegister(Drawable):
    def __init__(self, display, surface, name="Cash Register", color=colors["BLACK"], x=0, y=0, width=200, height=100):
        super().__init__(display, surface, name, color, x, y, width, height)
        self.body = self.makeBody()
        self.__free = True
        self.__info_text = Text(self.get_display(), self.get_surface(), str("Press B key for buy new ticket!"), colors["BLUE"], surface.get_width() - 160, 20, 10, 10, 15)
    def makeBody(self):
        return [
                Rectangle(self.get_display(), self.get_surface(), "", self.get_color(), self.get_x(), self.get_y(), self.get_width(), self.get_height()),
                Text(self.get_display(), self.get_surface(), self.get_name(), self.get_color(), self.get_x() + int(self.get_width()/4), self.get_y() +10, 10, 10)
                ]
    def change_color(self, color):
        self.set_color(color)
        if (self.get_color() == colors["RED"]):
            self.__free = False
        else:
            self.__free = True
        self.body = self.makeBody()
    def info(self):
        self.__info_text.draw()
    def draw(self):
        for part in self.body:
            part.draw()
        if not self.is_free():
            self.info()
    def is_free(self):
        return self.__free

class Circle(Drawable):
    def __init__(self, display, surface, name="Circle", color=colors["BLACK"], x=0, y=0, width = 50, height = 135):
        super().__init__(display, surface, name, color, x, y, width, height)
    def draw(self):
        pygame.draw.circle(self.get_display(), self.get_color(), (self.get_x() + int(self.get_width()/2), self.get_y()+int(self.get_height()/2)), int(self.get_height()), 3)

class Line(Drawable):
    def __init__(self, display, surface, name="Line", color=colors["BLACK"], startPoint=0, endPoint=0):
        super().__init__(display, surface, name, color, startPoint, endPoint)
        self.startPoint = startPoint
        self.endPoint = endPoint
    def draw(self):
        pygame.draw.line(self.get_display(), self.get_color(), self.startPoint, self.endPoint, 3)

class Rectangle(Drawable):
    def __init__(self, display, surface, name="Rectangle", color=colors["BLACK"], x=0, y=0, width = 50, height =50):
        super().__init__(display, surface,name,  color, x, y, width, height)
        self.__rect = (x, y, width, height)
    def draw(self):
        pygame.draw.rect(self.get_display(),self.get_color(),self.__rect, 3)

class Text(Drawable):
    def __init__(self, display, surface, name="Text", color=colors["BLACK"], x=0, y=0, width = 50, height =50, font_size = 25):
        super().__init__(display, surface,name, color, x, y, width, height)
        self.font = pygame.font.SysFont(None, font_size)
    def draw(self):
        screen_text = self.font.render(self.get_name(), True, self.get_color())
        self.get_display().blit(screen_text, [self.get_x(), self.get_y()])

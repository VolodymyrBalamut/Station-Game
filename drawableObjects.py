from figures import *

class Drawable:
    def __init__(self, display, surface, name="Drawable", color=(0,0,0), x=0, y=0, width = 25, height = 80):
        self.__display = display
        self.__surface = surface
        self.__name = name
        self.__color = color
        self.__x = x
        self.__y = y
        self.width = width
        self.height = height
    def draw(self):
        pass
    def current_pos(self):
        return str("( X= " + str(self.__x) + ", Y = " + str(self.__y) + " )") 
    def get_display(self):
        return self.__display
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_color(self, color):
        self.__color = color
    def get_color(self):
        return self.__color  
    def set_x(self, x):
        self.__x = x
        self.__check_border()
    def move_x(self, x):
        self.__x += x
        self.__check_border()
    def get_x(self):
        return self.__x
    def set_y(self, y):
        self.__y = y
    def move_y(self, y):
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


class Person(Drawable):
    def __init__(self, display, surface, name="John", color=(0,0,0), x=0, y=0):
        super().__init__(display, surface, name, color, x, y)
        self.name = "Person " + name
        self.body = self.makeBody()
    def myfunc(self):
        print("Hello my name is " + self.name)
    def makeBody(self):
        part_size = int(self.height / 8)
        return [
                 Circle(self.get_display(), self.get_color(), self.get_x(), self.get_y(), self.width, part_size),
                 Line(self.get_display(), self.get_color(), (self.get_x()+int(self.width / 2), self.get_y()+part_size), (self.get_x()+ int(self.width / 2), self.get_y() + 5*part_size)),
                 Line(self.get_display(), self.get_color(), (self.get_x(), self.get_y()+3*part_size), (self.get_x()+self.width, self.get_y()+3*part_size)),
                 Line(self.get_display(), self.get_color(), (self.get_x()+int(self.width / 2), self.get_y()+5*part_size), (self.get_x(), self.get_y()+self.height)),
                 Line(self.get_display(), self.get_color(), (self.get_x()+int(self.width / 2), self.get_y()+5*part_size), (self.get_x()+self.width, self.get_y()+self.height)),
                 Text(self.get_display(), self.get_color(), self.get_x(), self.get_y()+self.height +10, self.name)
                ]
    def draw(self):
        for part in self.body:
            part.draw()
    def changePosition(self):
        self.body = self.makeBody()

class Passenger(Person):
    def __init__(self, display, surface, name="John", color=(0,0,0), x=0, y=0):
        super().__init__(display, surface, name, color, x, y)
        self.name = "Passenger " + name
    
class Ticket(Drawable):
    def __init__(self, display, surface, name="Ticket", color=(0,0,0), x=0, y=0, width = 10, height = 10):
        super().__init__(display, surface,  name, color, x, y, width, height)
        self.body = self.makeBody()
        self.__ticket_count = 0
    def makeBody(self):
        return [
                 Rectangle(self.get_display(), self.get_color(), self.get_x(), self.get_y(), self.width, self.height),
                 Text(self.get_display(), self.get_color(), self.get_x(), self.get_y() +self.height + 10, self.get_name())
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

class CashRegister(Drawable):
    def __init__(self, display, surface, name="Cash Register", color=(0,0,0), x=0, y=0, width=200, height=100):
        super().__init__(display, surface, name, color, x, y, width, height)
        self.body = self.makeBody()
        self.__free = True
        self.__info_text = Text(self.get_display(), (0,0,0), surface.get_width() - 160, 20, str("Press B key for buy new ticket!"), 15)
    def makeBody(self):
        return [
                Rectangle(self.get_display(), self.get_color(), self.get_x(), self.get_y(), self.width, self.height),
                Text(self.get_display(), self.get_color(), self.get_x() + int(self.width/4), self.get_y() +10, self.get_name())
                ]
    def change_color(self, color):
        self.set_color(color)
        if (self.get_color() == (255,0,0)):
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

from figures import *

class Drawable:
    def __init__(self, name, display, color, x, y, width = 25, height = 80):
        self.display = display
        self.name = name
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def draw(self):
        pass

class Person(Drawable):
    def __init__(self, name, display, color, x, y):
        super().__init__(name, display, color, x, y)
        self.name = "Person " + name
        self.body = self.makeBody()
    def myfunc(self):
        print("Hello my name is " + self.name)
    def makeBody(self):
        part_size = int(self.height / 8)
        return [
                 Circle(self.display, self.color, self.x, self.y, self.width, part_size),
                 Line(self.display, self.color, (self.x+int(self.width / 2), self.y+part_size), (self.x+ int(self.width / 2), self.y+ 5*part_size)),
                 Line(self.display, self.color, (self.x, self.y+3*part_size), (self.x+self.width, self.y++3*part_size)),
                 Line(self.display, self.color, (self.x+int(self.width / 2), self.y+5*part_size), (self.x, self.y+self.height)),
                 Line(self.display, self.color, (self.x+int(self.width / 2), self.y+5*part_size), (self.x+self.width, self.y+self.height)),
                 Text(self.display, self.color, self.x, self.y+self.height +10, self.name)
                ]
    def draw(self):
        for part in self.body:
            part.draw()

class Passenger(Person):
    def __init__(self, name, display, color, x, y):
        super().__init__(name, display, color, x, y)
        self.name = "Passenger " + name
    def changePosition(self, x, y):
        self.x = x
        self.y = y
        self.body = self.makeBody()

class Ticket(Drawable):
    def __init__(self, name, display, color, x, y):
        super().__init__(name, display, color, x, y)
        self.body = [
                    Rectangle(display, color, x, y),
                    Text(self.display, self.color, self.x, self.y +10, self.name)
                     ]
    def draw(self):
        for part in self.body:
            part.draw()

class CashRegister(Drawable):
    def __init__(self, name, display, color, x, y, width=200, height=100):
        super().__init__(name, display, color, x, y, width, height)
        self.body = self.makeBody()
        self.isFree = 1
    def makeBody(self):
        return [
                Rectangle(self.display,self.color, self.x, self.y, self.width, self.height),
                Text(self.display, self.color, self.x + int(self.width/4), self.y +10, self.name)
                ]
    def changeColor(self, color):
        self.color = color
        self.body = self.makeBody()
    def draw(self):
        for part in self.body:
            part.draw()

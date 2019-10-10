import pygame
from figures import *

class Person:
    def __init__(self, name, display, color, x, y):
        self.name = name
        self.display = display
        self.color = color
        self.x = x
        self.y = y
        self.body = [
                     Circle(display, color, x, y),
                     Line(display, color, (self.x+25, self.y+50), (self.x+25, self.y+100)),
                     Line(display, color, (self.x, self.y+75), (self.x+50, self.y+75)),
                     Line(display, color, (self.x+25, self.y+100), (self.x, self.y+135)),
                     Line(display, color, (self.x+25, self.y+100), (self.x+50, self.y+135))
                     ]
    def myfunc(self):
        print("Hello my name is " + self.name)
    def draw(self):
        #pygame.draw.rect(self.display,self.color,(10,10,200,100),3)
        #pygame.draw.circle(self.display,self.color,(self.x+25, self.y+25),25, 3)
        #self.head.draw()
        for part in self.body:
            part.draw()
        #pygame.draw.line(self.display,self.color,(self.x+25, self.y+50), (self.x+25, self.y+100), 3)
        #pygame.draw.line(self.display, self.color,(self.x, self.y+75), (self.x+50, self.y+75), 3)
        #pygame.draw.line(self.display, self.color, (self.x+25, self.y+100), (self.x, self.y+135), 3)
        #pygame.draw.line(self.display, self.color, (self.x+25, self.y+100), (self.x+50, self.y+135), 3)

#(0, 100, 255)
#p1 = Person("John", 36)

#p1.myfunc()
#print(p1.name)
#print(p1.age)
#pygame.draw()

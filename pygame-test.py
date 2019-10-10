import pygame, sys
from pygame.locals import *
from person import Person
from ticket import Ticket

def main():
    pygame.init()

    DISPLAY=pygame.display.set_mode((500,400),0,32)

    WHITE=(255,255,255)
    BLUE=(0,0,255)
    BLACK=(0,0,0)

    DISPLAY.fill(WHITE)


    person = Person("John", DISPLAY, BLACK, 10, 10)
    person.draw()

    ticket = Ticket("Jocker", DISPLAY, BLACK, 100, 100)
    ticket.draw()

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

main()

import pygame, sys
from pygame.locals import *
from drawableObjects import Passenger, Ticket, CashRegister, Text
from datetime import datetime

WHITE=(255,255,255)
BLUE=(0,0,255)
BLACK=(0,0,0)
GREEN=(0,128,0)
RED=(255,0,0)

#setting screen
pygame.init()

pygame.display.set_caption('Station')

display_width = 500
display_height = 400
display_game=pygame.display.set_mode((display_width, display_height),0,32)

surface = pygame.display.get_surface()

w, h = surface.get_size()
print(w)

display_game.fill(WHITE)

step_size = 10
FPS = 15
clock = pygame.time.Clock()

def exit():
    print("Good bye")
    pygame.quit()
    sys.exit()

def draw_active_key(key):
    text = Text(display_game, BLACK, 5, 20, str(key))
    text.draw()

def info():
    text =  Text(display_game, BLACK, display_width - 160, 20, str("Press B key for buy new ticket!"), 15)
    text.draw()


lead_x_change = 0
lead_y_change = 0

person = Passenger(display_game, surface, "John", BLACK, int(display_width / 2), int(display_height / 2))
ticket = Ticket(display_game, surface, "Ticket", BLACK, display_width - 80, display_height - 80, 20, 20)
cash_register = CashRegister(display_game, surface, "Cash Register", GREEN, 100, 10)

#log files
f = open("logo.txt", "a")
f.write("Station logs! " + str(datetime.now().strftime("%x - %X")) + "\n")

active_key = ""
ticket_count = 0

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            f.close()
            exit()
        if event.type==KEYDOWN:
            if event.key==K_LEFT:
                lead_x_change = -step_size
                active_key = "Left"
                temp = active_key + " " + person.current_pos()
                f.write(temp+ "\n")
                print(temp)
            elif event.key==K_RIGHT:
                lead_x_change = step_size
                active_key = "Right"
                temp = active_key + " " + person.current_pos() 
                f.write(temp + "\n")
                print(temp)
            elif event.key==K_UP:
                lead_y_change = -step_size
                active_key = "Up"
                temp = active_key + " " + person.current_pos()
                f.write(temp + "\n")
                print(temp)
            elif event.key==K_DOWN:
                lead_y_change = step_size
                active_key = "Down"
                temp = active_key + " " + person.current_pos()
                f.write(temp + "\n")
                print(temp)
            elif event.key==K_b and cash_register.color == RED:
                ticket_count += 1
                active_key = "B"
                temp = "You have bought new ticket! You have " + str(ticket_count) + " tickets"
                f.write(temp + "\n")
                print(temp)
        if event.type==KEYUP:
            if event.key==K_LEFT or event.key==K_RIGHT:
                lead_x_change = 0
            elif event.key==K_UP or event.key==K_DOWN:
                lead_y_change = 0
    if (person.get_x() >= cash_register.get_x() and person.get_x() <= cash_register.get_x() + cash_register.width):
        if (person.get_y() >= cash_register.get_y() and person.get_y() <= cash_register.get_y() + cash_register.height):
            cash_register.changeColor(RED)
        else:
            cash_register.changeColor(GREEN)
    if (person.get_x() < cash_register.get_x() or person.get_x() > cash_register.get_x() + cash_register.width):
        cash_register.changeColor(GREEN)
    #if (person.get_x() < 0 or person.get_x() >= display_width or person.get_y() < 0 or person.get_y() >= display_height):
      #  f.close()
     #   exit()
    #move person
    person.move_x(lead_x_change)
    person.move_y(lead_y_change)

    person.changePosition()

    display_game.fill(WHITE)
    if cash_register.color == RED:
        info()
    person.draw()
    cash_register.draw()
    ticket.changeName("Tickets " + str(ticket_count))
    ticket.draw()
    draw_active_key(active_key)
    pygame.display.update()
    clock.tick(FPS)
import pygame, sys
from pygame.locals import *
from drawableObjects import Passenger, Ticket, CashRegister, Text
from logs import Logs

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

display_game.fill(WHITE)

step_size = 10
FPS = 15
clock = pygame.time.Clock()

def draw_active_key(key):
    text = Text(display_game, BLACK, 5, 20, str(key))
    text.draw()

lead_x_change = 0
lead_y_change = 0

person = Passenger(display_game, surface, "John", BLACK, int(display_width / 2), int(display_height / 2))
ticket = Ticket(display_game, surface, "Ticket", BLACK, display_width - 80, display_height - 80, 20, 20)
cash_register = CashRegister(display_game, surface, "Cash Register", GREEN, 100, 10)

objects = (person, ticket, cash_register)

logs = Logs()

active_key = ""
ticket_count = 0

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            logs.close()
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_LEFT:
                lead_x_change = -step_size
                active_key = "Left"
                temp = active_key + " " + person.current_pos()
                logs.write(temp)
            elif event.key==K_RIGHT:
                lead_x_change = step_size
                active_key = "Right"
                temp = active_key + " " + person.current_pos() 
                logs.write(temp)
            elif event.key==K_UP:
                lead_y_change = -step_size
                active_key = "Up"
                temp = active_key + " " + person.current_pos()
                logs.write(temp)
            elif event.key==K_DOWN:
                lead_y_change = step_size
                active_key = "Down"
                temp = active_key + " " + person.current_pos()
                logs.write(temp)
            elif event.key==K_b and (not cash_register.is_free()):
                ticket.ticket_inc()
                active_key = "B"
                temp = "You have bought new ticket! You have " + str(ticket.get_ticket_count()) + " tickets"
                logs.write(temp)
        if event.type==KEYUP:
            if event.key==K_LEFT or event.key==K_RIGHT:
                lead_x_change = 0
            elif event.key==K_UP or event.key==K_DOWN:
                lead_y_change = 0
    if (person.get_x() >= cash_register.get_x() and person.get_x() <= cash_register.get_x() + cash_register.width):
        if (person.get_y() >= cash_register.get_y() and person.get_y() <= cash_register.get_y() + cash_register.height):
            cash_register.change_color(RED)
        else:
            cash_register.change_color(GREEN)
    if (person.get_x() < cash_register.get_x() or person.get_x() > cash_register.get_x() + cash_register.width):
        cash_register.change_color(GREEN)
    
    #move person
    person.move_x(lead_x_change)
    person.move_y(lead_y_change)

    person.changePosition()

    display_game.fill(WHITE)
    #person.draw()
    #cash_register.draw()
    #ticket.draw()
    for obj in objects:
        obj.draw()
    draw_active_key(active_key)
    pygame.display.update()
    clock.tick(FPS)
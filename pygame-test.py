import pygame, sys
from pygame.locals import *
from drawableObjects import *



def exit():
    print("Good bye")
    pygame.quit()
    sys.exit()

def main():
    pygame.init()

    pygame.display.set_caption('Station')

    display_width = 500
    display_height = 400
    DISPLAY=pygame.display.set_mode((display_width, display_height),0,32)

    WHITE=(255,255,255)
    BLUE=(0,0,255)
    BLACK=(0,0,0)
    GREEN=(0,128,0)
    RED=(255,0,0)

    DISPLAY.fill(WHITE)

    lead_x = int(display_width / 2)
    lead_y = int(display_height / 2)
    lead_x_change = 0
    lead_y_change = 0

    step_size = 10
    FPS = 15

    clock = pygame.time.Clock()

    person = Passenger("John", DISPLAY, BLACK, lead_x, lead_y)
    ticket = Ticket("Jocker", DISPLAY, BLACK, 10, 10)
    cash_register = CashRegister("Cash Register", DISPLAY, GREEN, 100, 10)

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                exit()
            if event.type==KEYDOWN:
                if event.key==K_LEFT:
                    lead_x_change = -step_size
                    print("Left " + str(lead_x))
                elif event.key==K_RIGHT:
                    lead_x_change = step_size
                    print("Right " + str(lead_x))
                elif event.key==K_UP:
                    lead_y_change = -step_size
                    print("Up " + str(lead_y))
                elif event.key==K_DOWN:
                    lead_y_change = step_size
                    print("Down" + str(lead_y))
            if event.type==KEYUP:
                if event.key==K_LEFT or event.key==K_RIGHT:
                    lead_x_change = 0
                elif event.key==K_UP or event.key==K_DOWN:
                    lead_y_change = 0
        if (lead_x >= cash_register.x and lead_x <= cash_register.x + cash_register.width):
            if (lead_y >= cash_register.y and lead_y <= cash_register.y + cash_register.height):
                cash_register.changeColor(RED)
            else:
                cash_register.changeColor(GREEN)

        if (lead_x < cash_register.x or lead_x > cash_register.x + cash_register.width):
            cash_register.changeColor(GREEN)


        if lead_x < 0 or lead_x >= display_width or lead_y < 0 or lead_y >= display_height:
            exit()

        lead_x += lead_x_change
        lead_y += lead_y_change
        person.changePosition(lead_x,lead_y)


        DISPLAY.fill(WHITE)
        person.draw()
        cash_register.draw()
        #ticket.draw()
        pygame.display.update()
        clock.tick(FPS)

main()

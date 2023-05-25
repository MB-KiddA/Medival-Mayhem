import pygame, os

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

icon_1_image = 0

def icons(): 

    if select > 4: #Makes Select loop
        select = 1
    if select < 1: # Makes Select Loop
        select = 4



def icon_movement(keys_pressed, icons):

    if keys_pressed[pygame.K_a]: #If a is pressed and doesn't go past selection
        select = select - 1 and pygame.time.wait(50)
    if keys_pressed[pygame.K_d]: #If d is pressed and doesn't go past slection
        select = select + 1 and pygame.time.wait(50)

def char_select():
    keys_pressed = pygame.key.get_pressed()
    icon_movement(keys_pressed, icons)


import pygame, os

WIDTH, HEIGHT = 800, 600
Screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Medieval Mayhem')
icon_1_image = 0

players = {1:'rouge.png', 2:'druid.png', 3:'warrior.png', 4:'frog.png'}
files = {1:'rouge', 2:'druid', 3:'warrior', 4:'frog'}


def main_menu():
    while True:
        
        for event in pygame.event.get():
            if event.type == quit:
                pygame.quit()

def select(s1, s2): 
    s1 = 2
    s2= 2

    if s1 > 4: #Makes Select loop
        s1 = 1
    if s1 < 1: # Makes Select Loop
        s1 = 4
    while s1 != s2:

        if s1 > s2:
            s2 = s1 and pygame.transform.rotate(icons, 45)
        if s2 > s1:
            s2 = s1 and pygame.transform.rotate(icons, 135)
        

def p1_icon_movement(keys_pressed, icons):

    if keys_pressed[pygame.K_a]: #If a is pressed and doesn't go past selection
        select = select - 1 and pygame.time.wait(150)
    if keys_pressed[pygame.K_d]: #If d is pressed and doesn't go past slection
        select = select + 1 and pygame.time.wait(150)
    if keys_pressed[pygame.K_SPACE]:
        pick = 1

def p2_icon_movement(keys_pressed, icons):

    if keys_pressed[pygame.K_LEFT]:
        Select = Select - 1 and pygame.time.wait(150)
    if keys_pressed[pygame.K_RIGHT]:
        Select = Select + 1 and pygame.time.wait(150)
    if keys_pressed[pygame.K_KP4]:
        pick = 2 


def char_select():
    pick = 0
    keys_pressed = pygame.key.get_pressed()
    while pick == 0:
        p1_icon_movement(keys_pressed, icons)

    while pick == 1:
        p2_icon_movement(keys_pressed, icons)
    
    while pick == 2:
        main()

def main():
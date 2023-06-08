import pygame, os
from spites import *

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Medieval Mayhem')



def draw_sprite():
    WIN.blit(Background_Menu, (0, 0))
    WIN.blit(Rouge_Icon_prite, 100, 600)


    pygame.display.update()


def p1_icon_movement(keys_pressed, s1):

    if keys_pressed[pygame.K_a]: #If a is pressed and doesn't go past selection
        s1 = s1 - 1 and pygame.time.wait(150)
    if keys_pressed[pygame.K_d]: #If d is pressed and doesn't go past slection
        s1 = s1 + 1 and pygame.time.wait(150)
    if keys_pressed[pygame.K_t or pygame.K_y or pygame.K_u]:
        char_select(pick = 1)

def p2_icon_movement(keys_pressed, s1,):

    if keys_pressed[pygame.K_LEFT]:
        s1 = s1- 1 and pygame.time.wait(150)
    if keys_pressed[pygame.K_RIGHT]:
        s1 = s1 + 1 and pygame.time.wait(150)
    if keys_pressed[pygame.K_KP4 or pygame.K_KP5 or pygame.K_KP6]:
        char_select(pick = 2)


def char_select(keys_pressed, s1, pick):   
    while pick == 0:
        p1_icon_movement(keys_pressed, s1)

    while pick == 1:
        p2_icon_movement(keys_pressed, s1)
    
    while pick == 2:
        print('Game')

def main_menu():
    pick = 0
    s1 = 2
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            keys_pressed = pygame.key.get_pressed()
            if event.type == quit:
                run = False
                pygame.quit()

            if s1 > 4: #Makes Select loop
                s1 = 1
            elif s1 < 1: # Makes Select Loop
                s1 = 4

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t or pygame.K_y or pygame.K_u:
                    pick += 1
                    if s1 == 1:
                        p1 = Warrior
                    elif s1 == 2:
                        p1 = Rouge
                    elif s1 == 3:
                        p1 = Druid
                    elif s1 == 4:
                        p1 = Frog
        
            if event.type == pygame.KEYDOWN:
                pick += 1
                if event.key == pygame.K_KP4 or pygame.K_KP5 or pygame.K_KP6:
                    if s1 == 1:
                        p2 = Warrior
                    elif s1 == 2:
                        p2 = Rouge
                    elif s1 == 3:
                        p2 = Druid
                    elif s1 == 4:
                        p2 = Frog
            char_select(keys_pressed, s1, pick)          
        
            draw_sprite()

main_menu()
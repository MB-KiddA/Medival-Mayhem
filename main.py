import pygame, os
from index import p1, p2, game
from spites import *
WIDTH, HEIGHT = 800, 600
Win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Medieval Mayhem')

def draw_sprite():
    Win.blit(Background_Menu, (0, 0))





def select(s1, s2): 

    if s1 > 4: #Makes Select loop
        s1 = 1
    if s1 < 1: # Makes Select Loop
        s1 = 4
        

def p1_icon_movement(keys_pressed, p1):

    if keys_pressed[pygame.K_a]: #If a is pressed and doesn't go past selection
        select = select - 1 and pygame.time.wait(150)
    if keys_pressed[pygame.K_d]: #If d is pressed and doesn't go past slection
        select = select + 1 and pygame.time.wait(150)
    if keys_pressed[pygame.K_SPACE]:
        pick = 1

def p2_icon_movement(keys_pressed, p2):

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
        p1_icon_movement(keys_pressed, p1)

    while pick == 1:
        p2_icon_movement(keys_pressed, p2)
    
    while pick == 2:
        game()

def main_menu():
    s1 = 2
    s2 = 2
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == quit:
                run = False
                pygame.quit()

        char_select()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t or pygame.K_y or pygame.K_u:
                if s1 == 1:
                    p1 = Warrior
                if s1 == 2:
                    p1 = Rouge
                if s1 == 3:
                    p1 = Druid
                if s1 == 4:
                    p1 = Frog
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP4 or pygame.K_KP5 or pygame.K_KP6:
                if select(s1) == 1:
                    p2 = Warrior
                if select(s1) == 2:
                    p2 = Rouge
                if select(s1) == 3:
                    p2 = Druid
                if select(s1) == 4:
                    p2 = Frog
        draw_sprite()

main_menu()
import pygame, os

WIDTH, HEIGHT = 800, 600
Screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Medieval Mayhem')
icon_1_image = 0


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
        



def p1_movement(keys_pressed, s1):

    if keys_pressed[pygame.K_a]: #If a is pressed and doesn't go past selection
        s1 = s1 - 1 and pygame.time.wait(50)
    if keys_pressed[pygame.K_d]: #If d is pressed and doesn't go past slection
        s1 = s1 + 1 and pygame.time.wait(50)
    
for event in pygame.event.get()

def p2_movement(keys_pressed, s1):

    if keys_pressed[pygame.K_LEFT]: #If a is pressed and doesn't go past selection
        s1 = s1 - 1 and pygame.time.wait(50)
    if keys_pressed[pygame.K_RIGHT]: #If d is pressed and doesn't go past slection
        s1 = s1 + 1 and pygame.time.wait(50)



def char_select(s1):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_t:
            p1 = s1


keys_pressed = pygame.key.get_pressed()
p1_movement(keys_pressed, icons)
p2_movement(keys_pressed, icons)


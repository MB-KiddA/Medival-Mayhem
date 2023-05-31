import pygame, os

pygame.init()
WIDTH, HEIGHT = 800, 600
Screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Medieval Mayhem')
clock = pygame.time.Clock()
dt = 0
run = True
Vel = 10

def p1_movement(keys_pressed, icons):

    if keys_pressed[pygame.K_a] and p1.x - Vel > 0:  # LEFT
        p1.x -= Vel
    if keys_pressed[pygame.K_d] and p1.x + Vel + p1.width < BORDER.x:  # RIGHT
        p1.x += Vel * dt
    if keys_pressed[pygame.K_w] and p1.y - Vel > 0:  # UP
        p1.y -= Vel * dt
    if keys_pressed[pygame.K_s] and p1.y + Vel + p1.height < HEIGHT - 15:  # DOWN
        p1.y += Vel * dt

def p2_movement(keys_pressed, icons):

    if keys_pressed[pygame.K_LEFT]: #If a is pressed and doesn't go past selection
        s1 = s1 - 1 and pygame.time.wait(50)
    if keys_pressed[pygame.K_RIGHT]: #If d is pressed and doesn't go past slection
        s1 = s1 + 1 and pygame.time.wait(50)


    



p1_sprite = pygame.transform.load(os.path.join('Characters', char_select ))

def game():
    while run:
        for event in pygame.event.get(): #Be Able to Exit The Game
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
        pygame.display.update() #Updates the Screen

        keys_pressed = pygame.key.get_pressed() # Controls
        p1_movement(keys_pressed, p1)
        p2_movement(keys_pressed, p2)
        

    dt = clock.tick(60) / 1000 #FPS And Deltatime 
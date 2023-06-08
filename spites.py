import pygame,os

PH, PW = 64, 64

druid_sprite = pygame.image.load(
    os.path.join('Sprites','Druid.png'))

Druid = pygame.transform.scale(
    druid_sprite, (PH, PW))

Druid_Icon_Sprite = pygame.image.load(
    os.path.join('Sprites', 'Druid_Icon.png'))

rouge_sprite = pygame.image.load(
    os.path.join('Sprites', 'Rouge.png'))

Rouge = pygame.transform.scale(
    rouge_sprite, (PH, PW))

Rouge_Icon_prite = pygame.image.load(
    os.path.join('Sprites','Rouge_Icon.png'))

warrior_sprite = pygame.image.load(
    os.path.join('Sprites', 'Warrior.png'))

Warrior = pygame.transform.scale(
    warrior_sprite, (PH, PW))

Warrior_Icon_Sprite = pygame.image.load(
    os.path.join('Sprites','Warrior_Icon.png'))

frog_sprite = pygame.image.load(
    os.path.join('Sprites', 'Frog.png'))

Frog = pygame.transform.scale(
    frog_sprite, (PH, PW))

Frog_Icon_Sprite = pygame.image.load(
    os.path.join('Sprites','Frog_Icon.png'))

Background_Menu = pygame.transform.scale(pygame.image.load(
    os.path.join('Sprites', 'Background_Menu.png')), (800, 600))

Background_Game = pygame.transform.scale(pygame.image.load(
    os.path.join('Sprites', 'Background_Game.png')), (800, 600))

Druid_Icon_Select = pygame.image.load(
    os.path.join('Sprites', 'Druid_Icon_Select.png'))

Rouge_Icon_Select = pygame.image.load(
    os.path.join('Sprites', 'Rouge_Icon_Select.png'))

Warrior_Icon_Select = pygame.image.load(
    os.path.join('Sprites', 'Warrior_Icon_Select.png'))

Frog_Icon_Select = pygame.image.load(
    os.path.join('Sprites', 'Frog_Icon_Select.png'))
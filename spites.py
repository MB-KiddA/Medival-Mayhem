import pygame,os

druid_sprite = pygame.image.load(
    os.path.join('Druid', 'Druid.png'))

Druid = pygame.transform.rotate(pygame.transform.scale(
    druid_sprite, (800, 600)), 270)

rouge_sprite = pygame.image.load(
    os.path.join('Rouge', 'Rouge.png'))

Rouge = pygame.transform.rotate(pygame.transform.scale(
    rouge_sprite, (800, 600)), 270)

warrior_sprite = pygame.image.load(
    os.path.join('Warrior', 'Warrior.png'))

Warrior = pygame.transform.rotate(pygame.transform.scale(
    warrior_sprite, (800, 600)), 270)

frog_sprite = pygame.image.load(
    os.path.join('Frog', 'Frog.png'))

Frog = pygame.transform.rotate(pygame.transform.scale(
    frog_sprite, (800, 600)), 270)

Background_Menu = pygame.image.load(
    os.path.join('Background', 'Background_Menu.png'))

Background_Game = pygame.image.load(
    os.path.join('Background', 'Background_Game'))
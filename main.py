import pygame, sys
from square import Square

pygame.init()
screen = pygame.display.set_mode((800, 600))
player = Square((0, 0, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            player.x -= 
        if event.key == pygame.K_DOWN:

        if event.key == pygame.K_LEFT:

        if event.key == pygame.K_RIGHT:

    pygame.draw.rect(screen, player.color, player.rect, 0)
    pygame.display.flip()
    screen.fill((255, 255, 255))
import pygame, sys
from sprite import Sprite
from rectangle import Rectangle
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
player = Sprite(0, 300, (63, 189, 21), 20, 0, 0)
bombs = []
shooter = Rectangle(750, 0, (255, 8, 12), 50, 600)
clock = pygame.time.Clock()

pygame.time.set_timer(pygame.USEREVENT+1, 100)
pygame.display.set_caption("Shoot!")

def shootFire():
    global bombs
    size = random.randint(25, 30)
    bombs.append(Sprite(750, random.randint(0, 600-size), (217, 153, 26), size, -10, 0))

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.USEREVENT+1:
            shootFire()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.yVelocity = -5
            if event.key == pygame.K_DOWN:
                player.yVelocity = 5
            if event.key == pygame.K_LEFT:
                player.xVelocity = -5
            if event.key == pygame.K_RIGHT:
                player.xVelocity = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.yVelocity = 0
            if event.key == pygame.K_DOWN:
                player.yVelocity = 0
            if event.key == pygame.K_LEFT:
                player.xVelocity = 0
            if event.key == pygame.K_RIGHT:
                player.xVelocity = 0
    for bomb in bombs:
        pygame.draw.rect(screen, bomb.color, bomb.getRect(), 0)
        bomb.move()
        if bomb.x + bomb.width < 0:
            bombs.remove(bomb)
    pygame.draw.rect(screen, shooter.color, shooter.getRect(), 0)
    pygame.draw.rect(screen, player.color, player.getRect(), 0)
    player.move()
    pygame.display.flip()
    screen.fill((78, 104, 191))
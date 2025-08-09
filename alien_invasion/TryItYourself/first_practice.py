import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("WINTERFELL")

pygame.image.load("Jon_Snow.bmp")

while True:
    screen.fill((0, 0, 255))

    pygame.image.load("Jon_Snow.bmp").blitme()
    pygame.display.flip()

    for event in pygame.event.get():
        if event == pygame.QUIT:
            sys.exit()
    
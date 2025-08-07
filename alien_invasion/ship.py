import pygame

class Ship():
    def __init__(self, screen):
        self.screen = screen

        # load the ship image
        self.image = pygame.image.load(images/space_ship.bmp)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        """ make image center """
        self.rect.center = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
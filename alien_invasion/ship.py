import pygame

class Ship():
    def __init__(self, screen):
        self.screen = screen

        # load the ship image
        self.image = pygame.image.load("images/space_ship_new.bmp")

        self.rect = self.image.get_rect() # get_rect() to access the surface’s rect attribute
        self.screen_rect = screen.get_rect()

        """ make image center """
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        # blitme() method, which will draw the image to the screen at the position specified by self.rect.
        self.screen.blit(self.image, self.rect) 
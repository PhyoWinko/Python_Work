import sys

import pygame

def check_events():
    """Respond to keypresses and mouse event"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
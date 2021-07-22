import pygame
from pygame import sprite
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class to represent a single alien in the fleet"""

    def __init__(self, ai_game):
        """Initialise the alien and set starting position"""
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact hoizontal position
        self.x = float(self.rect.x)
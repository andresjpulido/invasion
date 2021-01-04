import pygame
import random

from pygame.locals import (
    RLEACCEL,
)
from invasion.Settings import Settings


class Halcon(pygame.sprite.Sprite):
    """
    Define the cloud object extending pygame.sprite.Sprite
    Use an image for a better looking sprite
    """

    def __init__(self):
        super(Halcon, self).__init__()
        self.settings = Settings()
        self.surf = pygame.image.load(self.settings.IMG_HALCON).convert_alpha()
        #self.surf.set_colorkey((0,0,0), RLEACCEL)
        # The starting position is randomly generated
        x = random.randint(int(self.settings.SCREEN_WIDTH/4) + 20, int(self.settings.SCREEN_WIDTH /3))
        y = random.randint(0, self.settings.SCREEN_HEIGHT)
        self.rect = self.surf.get_rect(
            center=(x, y)
        )


    def update(self):
        """
        Move the ship based on a constant speed
        Remove it when it passes the left edge of the screen
        """
        self.rect.move_ip(-3, 0)
        if self.rect.right < 0:
            self.kill()

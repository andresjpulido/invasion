import pygame
import random
from pygame.locals import (
    RLEACCEL,
)
from invasion.constants import *


class Cube(pygame.sprite.Sprite):
    def __init__(self):
        super(Cube, self).__init__()
        self.surf = pygame.image.load("src/assets/images/base.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        x = random.randint(int(self.settings.SCREEN_WIDTH/4) + 20, self.settings.SCREEN_WIDTH + 100)
        y = random.randint(0, self.settings.SCREEN_HEIGHT)
        self.rect = self.surf.get_rect(
            center=(x, y)
        )

    # Move the cloud based on a constant speed
    # Remove it when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()

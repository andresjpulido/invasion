import pygame
import random

from pygame.locals import (
    RLEACCEL,
)
from invasion.Settings import Settings


class Cloud(pygame.sprite.Sprite):

    def __init__(self):
        """
        Define the cloud object extending pygame.sprite.Sprite
        Use an image for a better looking sprite
        """
        super(Cloud, self).__init__()
        self.settings = Settings()
        #self.settings.IMG_CLOUD
        self.surf = pygame.image.load("assets/images/cloud.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(self.settings.SCREEN_WIDTH + 20, self.settings.SCREEN_WIDTH + 100),
                random.randint(0, self.settings.SCREEN_HEIGHT),
            )
        )


    # Move the cloud based on a constant speed
    # Remove it when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()

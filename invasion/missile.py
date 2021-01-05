import pygame
import random
from invasion.constants import(
    LEFT
)
from pygame.locals import (
    RLEACCEL,
)
from invasion.settings import Settings


class Missile(pygame.sprite.Sprite):
    """
    Define the enemy object extending pygame.sprite.Sprite
    Instead of a surface, we use an image for a better looking sprite
    """

    def __init__(self, direction=LEFT, fromX=None, fromY=None, type=None):
        super(Missile, self).__init__()
        self.settings = Settings()
        self.direction = direction
        self.surf = pygame.image.load(self.settings.IMG_MISSILE).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # The starting position is randomly generated, as is the speed
        if fromX != None:
            self.rect = self.surf.get_rect(
                center=(fromX, fromY)
            )

        else:
            self.rect = self.surf.get_rect(
                center=(
                    random.randint(self.settings.SCREEN_WIDTH + 20, self.settings.SCREEN_WIDTH + 100),
                    random.randint(0, self.settings.SCREEN_HEIGHT),
                )
            )
        self.speed = random.randint(5, 20)

    # Move the enemy based on speed
    # Remove it when it passes the left edge of the screen
    def update(self):
        if self.direction == LEFT:
            self.rect.move_ip(-self.speed, 0)
        else:
            self.rect.move_ip(self.speed, 0)
        if self.rect.right < 0:
            self.kill()

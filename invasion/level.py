import pygame
from pygame.locals import (
    RLEACCEL,
)
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_F1,
    K_F2,
    K_F3,
    K_F4

)
from invasion.settings import Settings


class Level(pygame.sprite.Sprite):

    def __init__(self, num):
        super(Level, self).__init__()
        self.settings = Settings()
        filename = "assets/images/"+str(num)+".png"
        self.surf = pygame.image.load(filename).convert_alpha()
        #self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                580,
                5000 - num,
            )
        )



    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, -5)
            """
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
"""

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > self.settings.SCREEN_WIDTH:
            self.rect.right = self.settings.SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= self.settings.SCREEN_HEIGHT:
            self.rect.bottom = self.settings.SCREEN_HEIGHT


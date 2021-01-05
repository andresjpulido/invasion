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


class Background(pygame.sprite.Sprite):

    def __init__(self, idx, idy):

        super(Background, self).__init__()
        if idy == 0:
            if idx % 2 == 0:
                filename = "assets/images/background.png"
            else:
                filename = "assets/images/background-2.png"
        else:
            if idx % 2 == 0:
                filename = "assets/images/background-3.png"
            else:
                filename = "assets/images/background-4.png"

        self.surf = pygame.image.load(filename).convert()
        self.x = self.surf.get_rect().right * idx
        self.y = self.surf.get_rect().height*idy
        self.idx = idx
        self.idy = idy
        #self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()
        pygame.Rect.move_ip(self.rect, self.x, self.y)

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(-5, 0)

        self.rect.move_ip(-5, 0)

        if self.rect.right < 0:
            pygame.Rect.move_ip(self.rect, self.rect.width*2, 0)

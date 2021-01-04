import pygame
import random

from pygame.locals import (
    RLEACCEL,
)
from invasion.Settings import Settings
from invasion.Constants import *


class Spatial_Rock(pygame.sprite.Sprite):
    """
    Define the cloud object extending pygame.sprite.Sprite
    Use an image for a better looking sprite
    """

    def __init__(self, type):

        super(Spatial_Rock, self).__init__()
        self.settings = Settings()
        self.upper_bound = 0
        self.lower_bound = 0
        self.filename = None

        # assign bounds for the creation of objects
        if type == COMET:
            self.upper_bound = 0
            self.lower_bound = 100
            self.filename = self.settings.IMG_COMET

        elif type == ASTEROID:
            self.upper_bound = 100
            self.lower_bound = 200
            self.filename = self.settings.IMG_ASTEROID

        elif type == METEOR:
            self.upper_bound = 200
            self.lower_bound = 300
            self.filename = self.settings.IMG_METEOR

        else:
            raise ValueError(format)

        self.surf = pygame.image.load(self.filename).convert_alpha()
        #self.surf.set_colorkey((0,0,0), RLEACCEL)
        # The starting position is randomly generated
        x = int(self.settings.windows_size[0]+200)
        y = random.randint(self.upper_bound, self.lower_bound)
        self.rect = self.surf.get_rect(
            center=(x, y)
        )


    def update(self):
        """
        Move the ship based on a constant speed
        Remove it when it passes the left edge of the screen
        """
        self.rect.move_ip(-4, 0)


        image = pygame.transform.rotate(self.surf, 45)
        rot_rect = self.rect.copy()

        #self.surf = image
        self.rect = image.get_rect(center=image.get_rect(center=(rot_rect.centerx, rot_rect.centery)).center)

        """ rota sin centro
        rot_image = pygame.transform.rotate(self.surf, 1)
        rot_rect = self.rect.copy()
        rot_rect.center = rot_image.get_rect().center
        self.surf = rot_image.subsurface(rot_rect).copy()
        """

        """ rota pero se jode la memoria 
        image = pygame.transform.rotate(self.surf, 45)
        self.rect = image.get_rect(center=self.surf.get_rect(center=(self.rect.centerx, self.rect.centery)).center)
        self.surf = image
        """


        if self.rect.right < 0:
            self.kill()


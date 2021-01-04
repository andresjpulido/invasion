from invasion.Constants import *

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

from invasion.Missile import Missile
from invasion.sounds import *
from invasion.Settings import Settings


class Player(pygame.sprite.Sprite):
    """
    Define the Player object extending pygame.sprite.Sprite
    Instead of a surface, we use an image for a better looking sprite
    """

    def __init__(self, game, height, width):
        super(Player, self).__init__()
        self.game = game
        self.settings = Settings()
        self.surf = pygame.image.load(self.settings.IMG_STARSHIP).convert_alpha()
        #self.surf.set_colorkey((0,0,0), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(width, height)
        self.direction = LEFT

    # Move the sprite based on keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
            move_up_sound.play()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            move_down_sound.play()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
            self.direction = LEFT
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
            self.direction = RIGHT
        if pressed_keys[K_F1]:
            shoot_laser_sound.play()
            if self.direction == LEFT:
                LEFT
            else:
                RIGHT
            new_missile = Missile(self.direction, self.rect.centerx, self.rect.centery)
            self.game.missiles.add(new_missile)
            self.game.all_sprites.add(new_missile)
        if pressed_keys[K_F2]:
            shoot_torpedo_sound.play()
        if pressed_keys[K_F3]:
            shoot_bomb_sound.play()
        if pressed_keys[K_F4]:
            shoot_laser_sound.play()

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > self.settings.SCREEN_WIDTH:
            self.rect.right = self.settings.SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= self.settings.SCREEN_HEIGHT:
            self.rect.bottom = self.settings.SCREEN_HEIGHT

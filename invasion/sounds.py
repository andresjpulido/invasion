import pygame

# Setup for sounds, defaults are good
pygame.mixer.init()

pygame.mixer.music.load("assets/sounds/Strange Stuff - Matt Harris.ogg")

# Load all our sound files
move_up_sound = pygame.mixer.Sound("assets/sounds/Rising_putter.ogg")
move_down_sound = pygame.mixer.Sound("assets/sounds/Falling_putter.ogg")
collision_sound = pygame.mixer.Sound("assets/sounds/Collision.ogg")
shoot_laser_sound = pygame.mixer.Sound("assets/sounds/laser2.ogg")
shoot_torpedo_sound = pygame.mixer.Sound("assets/sounds/laser1.ogg")
shoot_bomb_sound = pygame.mixer.Sound("assets/sounds/bomb.ogg")

# Set the base volume for all sounds
move_up_sound.set_volume(0.5)
move_down_sound.set_volume(0.5)
collision_sound.set_volume(0.5)

def music_play():
    pygame.mixer.music.play(loops=-1)

def music_volume_up():
    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.1)

def music_volume_down():
    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.1)

def music_pause():
    pygame.mixer.music.pause()

def music_unpause():
    pygame.mixer.music.unpause()

def collition():
    move_up_sound.stop()
    move_down_sound.stop()
    collision_sound.play()
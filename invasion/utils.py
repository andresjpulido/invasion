from random import randrange
import pygame

def random_color():
    """
    Return a random color.
    :return: Color tuple
    :rtype: tuple
    """
    return randrange(0, 255), randrange(0, 255), randrange(0, 255)


def rot_center(image, angle, x, y):
    """
    Extended description of function.
    Args:
        image (int): Object game
        angle (int): angle
        x (int): position x
        y (int): position y
    Returns:
        bool: Description of return value
    """

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=(x, y)).center)

    return rotated_image, new_rect
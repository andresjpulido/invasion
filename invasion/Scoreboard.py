import pygame.font
from pygame.sprite import Group
from pygame.locals import (
    RLEACCEL,
)

from invasion.ship_icon import Ship


class Scoreboard:
    """The class that reports scoring info."""

    def __init__(self, game):
        """Initialize the scoreboard attributes."""
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.player = game.player
        self.settings = game.settings
        self.stats = game.stats
        self.font = pygame.font.SysFont(None, 16)
        self.text_color = (255, 255, 255)
        # Prepare the score images
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_altitude()
        self.prep_ships()

    def prep_score(self):
        """Render the score to an image."""
        rounded_score = round(self.stats.score, -1)
        score_str = "Score: {:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        self.score_image.set_colorkey(self.settings.bg_color, RLEACCEL)
        # Put the score image at the top right corner.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_ships(self):
        """Show the remaining ships."""
        self.ships = Group()
        print("updating self.stats.ships_left " + str(self.stats.ships_left))
        for i in range(self.stats.ships_left):
            ship = Ship(self.game)
            ship.rect.x = 10 + i * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_high_score(self):
        """Render the high score to an image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "High Score: {:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)
        self.high_score_image.set_colorkey(self.settings.bg_color, RLEACCEL)
        # Put the high score image at the top center.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20

    def prep_level(self):
        """Render the level to an image"""
        level_str = "Level: " + str(1)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)
        self.level_image.set_colorkey(self.settings.bg_color, RLEACCEL)
        # Put the level image below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_altitude(self):
        """Render the level to an image"""
        level_str = "Altitude: " + str(5000 - self.player.rect.top)
        self.altitude_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)
        self.altitude_image.set_colorkey(self.settings.bg_color, RLEACCEL)
        # Put the level image below the score.
        self.altitude_rect = self.altitude_image.get_rect()
        self.altitude_rect.right = self.score_rect.right
        self.altitude_rect.top = self.score_rect.bottom + 30

    def draw_score(self):
        """Draw the scores, the level, and the remaining ships to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.altitude_image, self.altitude_rect)
        self.ships.draw(self.screen)


import pygame_menu
import os
import time
from invasion.settings import Settings
from invasion.constants import (
    COMET,
    ASTEROID,
    METEOR
)
from invasion.statistic import Statistic
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_PAGEUP,
    K_PAGEDOWN,
    K_F5
)
from invasion.sounds import *
from invasion.missile import Missile
from invasion.cloud import Cloud
from invasion.player import Player
from invasion.scoreboard import Scoreboard
from invasion.background import Background
from invasion.level import Level
from invasion.destroyer import Destroyer
from invasion.spatial_Rock import Spatial_Rock
from invasion.ghost import Ghost
from invasion.halcon import Halcon
from invasion.terminator import Terminator
from invasion.custom_events import CustomEvents

class Invasion:

    def __init__(self):
        """Initialize the game."""

        pygame.init()

        self.settings = Settings()
        self.events = CustomEvents()
        self.screen = pygame.display.set_mode((self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT))
        self.surface = pygame.display.set_mode(self.settings.WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        self.stats = Statistic(self)
        # position of the player
        height = self.surface.get_height()/2
        width = self.surface.get_width()/4

        # Create groups to hold enemy sprites, cloud sprites, and all sprites
        # - enemies is used for collision detection and position updates
        # - clouds is used for position updates
        # - all_sprites isused for rendering
        self.missiles = pygame.sprite.Group()
        self.clouds = pygame.sprite.Group()
        self.levels = pygame.sprite.Group()
        self.destroyers = pygame.sprite.Group()
        self.ghosts = pygame.sprite.Group()
        self.terminators = pygame.sprite.Group()
        self.halcons = pygame.sprite.Group()
        self.hunters = pygame.sprite.Group()
        self.bg = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.spatial_rocks = pygame.sprite.Group()

        # Create our 'player'
        self.player = Player(self, height, width)
        self.scoreboard = Scoreboard(self)

        pygame.display.set_caption('Invasion')
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        clock = pygame.time.Clock()

        program_icon = pygame.image.load(self.settings.IMG_ICON)
        pygame.display.set_icon(program_icon)

        music_play()

        self.main_menu = None
        self.create_menus()
    ###################################################


    def run(self):
        """Start the main loop for the program."""
        while True:
            self.clock.tick(self.settings.FPS)
            self.main_background()

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()

            self.main_menu.mainloop(self.surface)
            pygame.display.flip()
            """self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()"""

    def change_difficulty(self, value, difficulty):
        """
        Change difficulty of the game.
        :param value: Tuple containing the data of the selected object
        :type value: tuple
        :param difficulty: Optional parameter passed as argument to add_selector
        :type difficulty: str
        :return: None
        """
        selected, index = value
        print('Selected difficulty: "{0}" ({1}) at index {2}'.format(selected, difficulty, index))
        self.settings.DIFFICULTY[0] = difficulty

    def start_game(self):

        isActive = True
        clock = pygame.time.Clock()

        music_unpause()

        ######################################### events


        for x in range(0, 2):
            for y in range(0, 2):
                background = Background(x, y)
                self.bg.add(background)
                self.all_sprites.add(background)

        for i in range(0, 5000):
            if i % 50 == 0:
                level = Level(i)
                self.all_sprites.add(level)
                self.levels.add(level)

        self.all_sprites.add(self.player)

        running = True
        self.main_menu.disable()
        self.main_menu.reset(1)

        self.surface.fill((0, 0, 0))
        # Flip everything to the display
        pygame.display.flip()

        while running:
            # Look at every event in the queue
            for event in pygame.event.get():
                # Did the user hit a key?
                if event.type == KEYDOWN:
                    # Was it the Escape key? If so, stop the loop
                    if event.key == K_ESCAPE:
                        #running = False
                        music_pause()
                        self.pause_menu.mainloop(self.surface)

                    elif event.key == K_PAGEUP:
                        music_volume_up()

                    elif event.key == K_PAGEDOWN:
                        music_volume_down()

                # Did the user click the window close button? If so, stop the loop
                elif event.type == QUIT:
                    running = False

                # Should we add a new enemy?
                elif event.type == self.events.add_missile_event:
                    # Create the new enemy, and add it to our sprite groups
                    new_missile = Missile()
                    self.missiles.add(new_missile)
                    self.all_sprites.add(new_missile)

                # Should we add a new cloud?
                elif event.type == self.events.add_cloud_event:
                    # Create the new cloud, and add it to our sprite groups
                    new_cloud = Cloud()
                    self.clouds.add(new_cloud)
                    self.all_sprites.add(new_cloud)

                elif event.type == self.events.add_destroyer_event:
                    new_destroyer = Destroyer()
                    self.destroyers.add(new_destroyer)
                    self.all_sprites.add(new_destroyer)

                elif event.type == self.events.add_ghost_event:
                    new_ghost = Ghost()
                    self.ghosts.add(new_ghost)
                    self.all_sprites.add(new_ghost)

                elif event.type == self.events.add_terminator_event:
                    new_terminator = Terminator()
                    self.terminators.add(new_terminator)
                    self.all_sprites.add(new_terminator)

                elif event.type == self.events.add_halcon_event:
                    new_halcon = Halcon()
                    self.halcons.add(new_halcon)
                    self.all_sprites.add(new_halcon)

                elif event.type == self.events.add_hunter_event:
                    new_hunter = Halcon()
                    self.hunters.add(new_hunter)
                    self.all_sprites.add(new_hunter)

                elif event.type == self.events.add_asteroid_event:
                    new_spatial_rock = Spatial_Rock(ASTEROID)
                    self.spatial_rocks.add(new_spatial_rock)
                    self.all_sprites.add(new_spatial_rock)

                elif event.type == self.events.add_comet_event:
                    new_spatial_rock = Spatial_Rock(COMET)
                    self.spatial_rocks.add(new_spatial_rock)
                    self.all_sprites.add(new_spatial_rock)

                elif event.type == self.events.add_meteor_event:
                    new_spatial_rock = Spatial_Rock(METEOR)
                    self.spatial_rocks.add(new_spatial_rock)
                    self.all_sprites.add(new_spatial_rock)

                elif event.type == self.events.invoke_transition_event:
                    self.stats.ships_left = self.stats.ships_left - 1
                    self.scoreboard.prep_ships()
                    # draw the transition

                    self.screen.fill((255, 0, 0, 0))
                    time.sleep(2)
                    # continue the game

                    if self.stats.ships_left == 0:
                        self.transition_menu.mainloop(self.surface)

                    #clean
                    self.screen.fill((0, 0, 0, 0))
                    self.player.kill()

                    for x in range(0, 2):
                        for y in range(0, 2):
                            background = Background(x, y)
                            self.bg.add(background)
                            self.all_sprites.add(background)

                    for i in range(0, 5000):
                        if i % 50 == 0:
                            level = Level(i)
                            self.all_sprites.add(level)
                            self.levels.add(level)

                    height = self.surface.get_height() / 2
                    width = self.surface.get_width() / 4

                    self.spatial_rocks.empty()
                    self.player = Player(self, height, width)
                    self.scoreboard.prep_level()
                    self.all_sprites.add(self.player)
                    self.spatial_rocks.update()
                    isActive = True




            # Get the set of keys pressed and check for user input
            pressed_keys = pygame.key.get_pressed()
            self.player.update(pressed_keys)

            # Update the position of all objects
            self.missiles.update()
            self.clouds.update()
            self.terminators.update()
            self.destroyers.update()
            self.ghosts.update()
            self.halcons.update()
            self.levels.update(pressed_keys)
            self.spatial_rocks.update()
            self.bg.update(pressed_keys)

            self.scoreboard.prep_altitude()

            # Draw all our sprites
            for entity in self.all_sprites:
                self.screen.blit(entity.surf, entity.rect)

            # Check if any enemies have collided with the player
            if (pygame.sprite.spritecollideany(self.player, self.destroyers) \
                    or pygame.sprite.spritecollideany(self.player, self.spatial_rocks) \
                    )and isActive:

                # If so, remove the player
                # self.player.kill()

                # Stop any moving sounds and play the collision sound
                collition()

                #TODO change the ship image
                #TODO change the object image
                # Stop the loop
                pygame.time.set_timer(self.events.invoke_transition_event, 500, True)
                isActive = False

            self.scoreboard.draw_score()

            # Flip everything to the display
            pygame.display.flip()

            # Ensure we maintain a 30 frames per second rate
            clock.tick(30)


        #self.main_menu.enable()
        #self.main_menu.reset(1)

    def main_background(self):
        """
        Function used by menus, draw on background while menu is active.
        :return: None
        """

        self.surface.fill((128, 128, 128))

    def create_menus(self):
        bg_image_menu = pygame_menu.baseimage.BaseImage(
            image_path=self.settings.IMG_MAIN_MENU,
            drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
            drawing_offset=(0, 0)
        )

        main_theme = pygame_menu.themes.THEME_SOLARIZED.copy()
        main_theme.menubar_close_button = False  # Disable close button
        main_theme.background_color = bg_image_menu
        main_theme.title_shadow = False
        main_theme.title_background_color = (4, 47, 58)
        main_theme.widget_font = pygame_menu.font.FONT_8BIT
        main_theme.title_font = pygame_menu.font.FONT_FRANCHISE
        main_theme.widget_shadow = False
        main_theme.widget_font_size = 15
        main_theme.widget_font_color = (38, 158, 151)
        main_theme.selection_color = (255, 255, 255)

        self.main_menu = pygame_menu.Menu(
            height=self.settings.WINDOW_SIZE[1] * 0.6,
            onclose=pygame_menu.events.DISABLE_CLOSE,
            theme=main_theme,
            title='Main Menu',
            width=self.settings.WINDOW_SIZE[0] * 0.6
        )
        # -------------------------------------------------------------------------
        # Create menus: Play Menu
        # -------------------------------------------------------------------------
        play_submenu = pygame_menu.Menu(
            height=self.settings.WINDOW_SIZE[1] * 0.6,
            onclose=pygame_menu.events.DISABLE_CLOSE,
            theme=main_theme,
            title='Submenu',
            width=self.settings.WINDOW_SIZE[0] * 0.6,
        )
        play_submenu.add_button('Return to main menu', pygame_menu.events.BACK)

        play_menu = pygame_menu.Menu(
            height=self.settings.WINDOW_SIZE[1] * 0.6,
            onclose=pygame_menu.events.DISABLE_CLOSE,
            theme=main_theme,
            title='Play Menu',
            width=self.settings.WINDOW_SIZE[0] * 0.6,
        )

        play_menu.add_button('Start', self.start_game, )
        play_menu.add_selector('Select difficulty ',
                               self.settings.DIFFICULTIES,
                               onchange=self.change_difficulty,
                               selector_id='select_difficulty')
        play_menu.add_button('Another menu', play_submenu)
        play_menu.add_button('Return to main menu', pygame_menu.events.BACK)


        # -------------------------------------------------------------------------
        # Create menus:About
        # -------------------------------------------------------------------------
        about_menu = pygame_menu.Menu(
            height=self.settings.WINDOW_SIZE[1] * 0.6,
            onclose=pygame_menu.events.DISABLE_CLOSE,
            theme=main_theme,
            title='About',
            width=self.settings.WINDOW_SIZE[0] * 0.6,
        )
        for m in self.settings.ABOUT:
            about_menu.add_label(m, align=pygame_menu.locals.ALIGN_LEFT, font_size=10)
        about_menu.add_label('')
        about_menu.add_button('Return to menu', pygame_menu.events.BACK)

        # -------------------------------------------------------------------------
        # Create menus: Main
        # -------------------------------------------------------------------------
        self.main_menu.add_button('Play', play_menu)
        self.main_menu.add_button('About', about_menu)
        self.main_menu.add_button('Quit', pygame_menu.events.EXIT)

        self.pause_menu = pygame_menu.Menu(
            height=self.settings.WINDOW_SIZE[1] * 0.6,
            onclose=pygame_menu.events.DISABLE_CLOSE,
            theme=main_theme,
            title='Invasion',
            width=self.settings.WINDOW_SIZE[0] * 0.6,
        )

        self.pause_menu.add_label("" + str(self.stats.ships_left))
        self.pause_menu.add_label("Pause", align=pygame_menu.locals.ALIGN_CENTER, font_size=15)
        self.pause_menu.add_label("")
        self.pause_menu.add_label("")
        self.pause_menu.add_button('Continue', self.start_game)
        self.pause_menu.add_button('New game', play_menu)
        self.pause_menu.add_button('Quit', pygame_menu.events.EXIT)

        self.transition_menu = pygame_menu.Menu(
            height=self.settings.WINDOW_SIZE[1] * 0.6,
            onclose=pygame_menu.events.DISABLE_CLOSE,
            theme=main_theme,
            title='Invasion',
            width=self.settings.WINDOW_SIZE[0] * 0.6,
        )
        self.transition_menu.add_label("Game Over")
        self.transition_menu.add_label("")
        self.transition_menu.add_label("")
        self.transition_menu.add_button('New game', play_menu)





if __name__ == "__main__":
    # Create a game instance and run it
    program = Invasion()
    program.run()


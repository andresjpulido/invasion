class Settings:
    """
    The class to store all the settings for Invasion.
    """

    def __init__(self):
        """
        Initialize the static settings.
        """
        # Screen settings.
        self.screen_width = 10000
        self.screen_height = 5000
        self.windows_size = (640, 480)
        self.bg_color = (128, 0, 0)
        self.ship_limit = 3

        self.IMG_DESTROYER = "assets/images/destroyer.png"
        self.IMG_CLOUD = "assets/images/cloud.png"
        self.IMG_MISSILE = "assets/images/missile.png"
        self.IMG_STARSHIP = "assets/images/starship.png"
        self.IMG_SHIP_ICON = "assets/images/ship.bmp"
        self.IMG_GHOST = "assets/images/ghost.png"
        self.IMG_TERMINATOR = "assets/images/terminator.png"
        self.IMG_HALCON = "assets/images/halcon.png"
        self.IMG_HUNTER = "assets/images/hunter.png"

        self.IMG_ASTEROID = "assets/images/asteroid.png"
        self.IMG_METEOR = "assets/images/meteor.png"
        self.IMG_COMET = "assets/images/comet.png"

        self.IMG_MAIN_MENU = "assets/images/bg_menu.jpg"
        self.IMG_ICON = "assets/images/icon.png"

        self.SCREEN_WIDTH = 10000
        self.SCREEN_HEIGHT = 5000
        self.WINDOW_SIZE = (640, 480)
        self.ABOUT = ['Invasion',
            'Author: @andresjpb',
            'Email: andresjpulido@gmail.com']
        self.DIFFICULTY = ['EASY']
        self.FPS = 60.0
        self.DIFFICULTIES = [('1 - Easy', 'EASY'), ('2 - Medium', 'MEDIUM'), ('3 - Hard', 'HARD')]


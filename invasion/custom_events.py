import pygame


class CustomEvents:

    def __init__(self):

        # Create custom events for adding a new sprites
        self.add_missile_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.add_missile_event, 250)
        self.add_cloud_event = pygame.USEREVENT + 2
        pygame.time.set_timer(self.add_cloud_event, 50)
        self.add_destroyer_event = pygame.USEREVENT + 3
        pygame.time.set_timer(self.add_destroyer_event, 500)
        self.add_ghost_event = pygame.USEREVENT + 4
        pygame.time.set_timer(self.add_ghost_event, 250)
        self.add_terminator_event = pygame.USEREVENT + 5
        pygame.time.set_timer(self.add_terminator_event, 250)
        self.add_halcon_event = pygame.USEREVENT + 6
        pygame.time.set_timer(self.add_halcon_event, 250)
        self.add_hunter_event = pygame.USEREVENT + 6
        pygame.time.set_timer(self.add_hunter_event, 1250)
        self.add_meteor_event = pygame.USEREVENT + 7
        pygame.time.set_timer(self.add_meteor_event, 1000)
        self.add_asteroid_event = pygame.USEREVENT + 8
        pygame.time.set_timer(self.add_asteroid_event, 2000)
        self.add_comet_event = pygame.USEREVENT + 9
        pygame.time.set_timer(self.add_comet_event, 10000)
        self.invoke_transition_event = pygame.USEREVENT + 10
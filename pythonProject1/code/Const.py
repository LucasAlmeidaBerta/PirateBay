# C
import pygame

COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 188)
# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P ',
               'EXIT')
# S
SCREEN_WIDTH = 576
SCREEN_HEIGHT = 324
# E
ENTITY_SPEED = {'Level1BG0': 0,
                'Level1BG1': 0.5,
                'Level1BG2': 1,
                'Level1BG3': 2,
                'Player1': 2,
                'Player2': 2,
                'Enemy1': 1
                }
EVENT_ENEMY = pygame.USEREVENT + 1
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}

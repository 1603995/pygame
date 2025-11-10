import pygame
import random
from pygame.locals import RLEACCEL

from screen import Screen
from game_sprite import GameSprite
class Mountain(GameSprite):


    def __init__(self):
        super(Mountain, self).__init__()
        self.surf = pygame.image.load("icons/mountain.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # The starting position is randomly generated, as is the speed
        self.rect = self.surf.get_rect(
            center=(
                Screen.width,
                Screen.height-50,
            )
        )


    def clone(self):
        return Mountain()

    # Move the bird based on speed
    # Remove it when it passes the left edge of the screen.py

    def update(self):

        speed_x = -3
        speed_y = 0
        self.rect.move_ip(speed_x, speed_y)
        if self.rect.right < 0:
            self.kill()
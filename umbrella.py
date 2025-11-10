import pygame
import random
from game_sprite import GameSprite
from pygame.locals import RLEACCEL

from screen import Screen

class Umbrella(GameSprite):
    Max_Speed = 10
    Min_Speed = 5

    def __init__(self):
        super(Umbrella, self).__init__()
        self.surf = pygame.image.load("icons/umbrella.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # The starting position is randomly generated, as is the speed
        self.rect = self.surf.get_rect(
            center=(
                random.randint(0, Screen.width + 100),
                random.randint(0 , 20 ),
            )
        )
        self.speed = random.randint(self.Min_Speed, self.Max_Speed)

    def clone(self):
        return Umbrella()

    # Move the bird based on speed
    # Remove it when it passes the left edge of the screen.py

    def update(self):

        speed_x = -3# Sino los paraguas se van a la derecha y no los ves
        speed_y = self.speed

        self.rect.move_ip(speed_x, speed_y)
        if self.rect.bottom < 0:
            self.kill()
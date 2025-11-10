import random
import pygame

class FactorySprites:
    def __init__(self, prototypes, periods, base_event_type):
        self._prototypes = prototypes      # list[GameSprite]
        self._periods = periods            # list[int]
        self.event_types = []             # one per prototype

        for i, period in enumerate(periods):
            event_type = base_event_type + i
            pygame.time.set_timer(event_type, period)
            self.event_types.append(event_type)

    def make(self, event_type):
        return self._prototypes[event_type - self.event_types[0]].clone()

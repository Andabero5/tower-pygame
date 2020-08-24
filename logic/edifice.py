import pygame
from .floor import *


class Edifice(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)

    def addFloor(self, Floor):
        self.add(Floor)

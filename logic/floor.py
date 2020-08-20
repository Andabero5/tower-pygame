import pygame
from copy import copy, deepcopy
HEIGHT = 800
WIDTH = 500


class Floor():
    def __init__(self, imgFloor):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imgFloor)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.centery = 75
        self.speed = [5, 0]

    def update(self, opc=0):
        if opc == 1:
            self.speed = [0, 10]
        elif self.rect.right >= WIDTH or self.rect.left <= 0:
            self.speed[0] = -self.speed[0]
        if self.rect.bottom >= HEIGHT-53:
            self.speed[1] = 0
        self.rect.move_ip(self.speed)

    def clone(self):
        return deepcopy(self)

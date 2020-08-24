import pygame
from copy import copy, deepcopy
from random import choice
HEIGHT = 800
WIDTH = 500


class Floor(pygame.sprite.Sprite):
    def __init__(self, imgFloor):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imgFloor)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.centery = 75
        self.speed = [choice([5, -5]), 0]

    def update(self, fall=False, action=0, group=None):
        if fall == True:
            self.speed = [0, 10]
        elif self.rect.right >= WIDTH or self.rect.left <= 0:
            self.speed[0] = -self.speed[0]
        if action == 0:
            if self.rect.bottom >= HEIGHT-53:
                self.speed[1] = 0
        elif action == 1:
            list = pygame.sprite.spritecollide(self, group, False)
            if list:
                self.speed[1] = 0
                if self.rect.centerx >= list[0].rect.centerx+80 or self.rect.centerx <= list[0].rect.centerx-80:
                    list[0].kill()
                    self.remove()
                    self.speed[1] = 10

        self.rect.move_ip(self.speed)

    def clone(self):
        return copy(self)

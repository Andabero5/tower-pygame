import pygame
from .factoryMethod import FloorFactory
from .floor import *
from logic.fabrica import *
from logic.edifice import *


HEIGHT = 800
WIDTH = 500
FloorArray = []


CLOCK = pygame.time.Clock()


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tower Blocks")
    imagen_defondo = pygame.image.load("images\principalScene.png").convert()
    prototype = Prototype()
    floor = prototype.floorClone()
    edifice = Edifice()
    loop = True
    option = 0
    while loop == True:

        CLOCK.tick(60)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    floor.update(True)
        screen.blit(imagen_defondo, [0, 0])
        screen.blit(floor.image, floor.rect)
        if floor.speed == [0, 0]:
            edifice.addFloor(floor)
            floor = prototype.floorClone()
            option = 1
        if option > 0:
            floor.update(action=1, group=edifice)
        else:
            floor.update()
        edifice.draw(screen)
        edifice.update()

    pygame.quit()


if __name__ == "__main__":

    main()

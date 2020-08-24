import pygame
from factoryMethod import FloorFactory
from floor import Floor
from fabrica import *
from edifice import *


HEIGHT = 800
WIDTH = 500
FloorArray = []

screen = pygame.display.set_mode((WIDTH, HEIGHT))
imagen_defondo = pygame.image.load("images\principalScene.png").convert()
CLOCK = pygame.time.Clock()


def main():
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
                    floor.update(True, 1, edifice)
        screen.blit(imagen_defondo, [0, 0])
        screen.blit(floor.image, floor.rect)
        floor.update()
        if floor.rect.bottom > WIDTH/2:
            edifice.addFloor(floor)
            floor = prototype.floorClone()
        edifice.draw(screen)
        edifice.update()

    pygame.quit()


if __name__ == "__main__":
    main()

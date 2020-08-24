import pygame
from factoryMethod import FloorFactory
from floor import Floor
from fabrica import *
from time import sleep


HEIGHT = 800
WIDTH = 500
FloorArray = []

screen = pygame.display.set_mode((WIDTH, HEIGHT))
imagen_defondo = pygame.image.load("images\principalScene.png").convert()
CLOCK = pygame.time.Clock()


def main():
    prototype = Prototype()
    FloorArray.append(prototype.floorClone())
    loop = True
    number = 0
    option = 0
    while loop == True:
        CLOCK.tick(60)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    FloorArray[number].update(True)
        screen.blit(imagen_defondo, [0, 0])
        screen.blit(FloorArray[number].image, FloorArray[number].rect)
        for n in range(0, number+1):
            screen.blit(FloorArray[n].image, FloorArray[n].rect)
            if n > 0:
                FloorArray[n].update(action=1, floor=FloorArray[n-1])
            else:
                FloorArray[n].update()
            if FloorArray[number].speed == [0, 0]:
                FloorArray.append(prototype.floorClone())
                number += 1

    pygame.quit()


if __name__ == "__main__":
    main()

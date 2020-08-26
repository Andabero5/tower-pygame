import pygame
from .factoryMethod import FloorFactory
from .floor import *
from .prototype import *
from .edifice import *
from .chainOfResponsability import *

HEIGHT = 800
WIDTH = 500


CLOCK = pygame.time.Clock()


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tower Blocks")
    prototype = Prototype()
    floor = prototype.floorClone('yellowFloor')
    edifice = Edifice()
    chain = ChainFloor()
    imagen_defondo = chain.operacion(1)
    loop = True
    option = 0
    delete = False
    first = True
    pause = False
    floorCount = 0
    actualNum = 0
    pre = 0
    while loop == True:
        CLOCK.tick(60)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if pause == False:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        floor.update(True)
        imagen_defondo = chain.operacion(floorCount)
        screen.blit(imagen_defondo, [0, 0])
        screen.blit(floor.image, floor.rect)
        actualNum = len(edifice.sprites())
        if floor.rect.bottom > HEIGHT+50:
            pause = True
        if floor.speed == [0, 0]:
            edifice.addFloor(floor)
            floor = prototype.floorClone('yellowFloor')
            option = 1
            delete = False
            if actualNum >= pre:
                pre += 1
                floorCount += 1
                if actualNum % 5 == 0:
                    pre = 0
                imagen_defondo = chain.operacion(floorCount)
            if actualNum < pre:
                pre -= 1
                floorCount -= 1
        if delete:
            floor.update(action=2)
        elif option > 0:
            if actualNum == 6:
                if first:
                    first = False
                    edifice.empty()
                    delete = True
                else:
                    firstSprite = 0
                    for i in edifice.sprites():
                        if firstSprite == 0:
                            firstSprite += 1
                        else:
                            edifice.remove(i)
            else:
                floor.update(action=1, group=edifice)
        else:
            floor.update()
        edifice.draw(screen)
        edifice.update()
    pygame.quit()


if __name__ == "__main__":
    main()

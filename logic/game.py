import pygame
from .factoryMethod import FloorFactory
from .floor import *
from .ChainResponsability import *
from logic.prototype import *
from logic.edifice import *


HEIGHT = 800
WIDTH = 500


CLOCK = pygame.time.Clock()


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tower Blocks")
    
    prototype = Prototype()
    floor = prototype.floorClone('redFloor')
    edifice = Edifice()
    score = 0
    loop = True
    option = 0
    delete = False
    first = True
    chainFloor = ChainFloor()
    floorCount = 0
    while loop == True:
        CLOCK.tick(60)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    floor.update(True)
                    floorCount +=1
                    score +=10

        screen.blit(chainFloor.operacion(floorCount), [0, 0])
        screen.blit(floor.image, floor.rect)

        if floor.speed == [0, 0]:
            edifice.addFloor(floor)
            if floorCount <=7:
                floor = prototype.floorClone('redFloor')
            elif floorCount > 7 and floorCount <= 18:
                floor = prototype.floorClone('blueFloor')
            elif floorCount >18 and floorCount <= 26:
                floor = prototype.floorClone('greenFloor')
            elif floorCount >26:
                floor = prototype.floorClone('yellowFloor')
            option = 1
            delete = False
        if delete:
            floor.update(action=2)
        elif option > 0:
            if len(edifice.sprites()) == 7:
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

        #SCORE
        textScore = pygame.font.SysFont('comicsans black',30)
        texto = textScore.render("Puntaje: "+str(score), True, (0,0,0) )                                           
        screen.blit(texto, (350,8)) 

        edifice.draw(screen)
        edifice.update()

    pygame.quit()


if __name__ == "__main__":

    main()

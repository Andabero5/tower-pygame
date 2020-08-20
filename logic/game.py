import pygame
from AbstractFactory import FloorFactory
from floor import Floor
from prototype.fabrica import FloorCreator

HEIGHT = 800
WIDTH = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
imagen_defondo = pygame.image.load("images\principalScene.png").convert()
CLOCK = pygame.time.Clock()


def main():
    creator = FloorCreator()
    floor = creator.retrieveFloor('yellowFloor')
    loop = True
    while loop == True:
        CLOCK.tick(60)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    floor.update(1)
        screen.blit(imagen_defondo, [0, 0])
        screen.blit(floor.image, floor.rect)
        floor.update()
    pygame.quit()


if __name__ == "__main__":
    main()

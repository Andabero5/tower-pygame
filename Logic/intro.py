import pygame
from pygame.locals import *
import sys 
from Logic.FactoryMethod import *

#Constantes 
WIDHT = 380
HEIGHT = 600



class Floor():
    def __init__(self, floor_image):

        #Atributos

        #Carga la imagen
        self.image = pygame.image.load(floor_image).convert_alpha()

        #Tamaño de la imagen - Ancho y alto
        self.width_image, self.height_image = self.image.get_size()

        #Posición de la imagen del piso
        self.pos_x = WIDHT/2 - self.width_image/2
        self.pos_y = 25

        # Dirección de movimiento de Floor Image
        self.rect_x = 1
        self.rect_y = 0

    def movement(self):
        self.pos_x += self.rect_x

        if self.pos_x > WIDHT - self.width_image:
            self.rect_x*= -1
    
        if self.pos_x < 0:
            self.rect_x *=-1
        
        if self.pos_y < HEIGHT - (self.height_image + 40): 
            self.pos_y += self.rect_y
            


        

#Función principal
def main():

    pygame.init()
    screen = pygame.display.set_mode((WIDHT,HEIGHT))
    pygame.display.set_caption("Tower Blocks")

    #Se carga el fondo
    background = pygame.image.load("Images\Interface\Scenes\scene_Workspace.png").convert()
    
    factory = FloorFactory()
    floor = Floor(factory.getFloor(10))
   
    #Bucle principal

    playing = True
    
    while playing:

        floor.movement()
        screen.blit(background,[0,0])
        screen.blit(floor.image,(floor.pos_x, floor.pos_y))

        #Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = false
            
            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    playing = false

                if event.key == pygame.K_DOWN:
                    floor.rect_x = 0
                    floor.rect_y = 4

        #Actualizar
        pygame.display.flip()
        pygame.time.Clock().tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()






import pygame

#Set the Instructions as a list
def setInstructions():
    instruction=[]
    instruction.append("El objetivo de este videojuego es construir un edificio con la mayor cantidad de pisos posible,"\
        " estos pisos pueden de ser de tipo:")
    instruction.append("Residencial")
    instruction.append("Comercial")
    instruction.append("Oficinas")
    instruction.append("Lujo")
    return instruction

#Set the Pics of the houses
def setHouses():
    houses = []
    for i in range(1,5):
        house=pygame.image.load("Images/Interface/Towers/Floor-0"+str(i)+".png")
        houses.append(pygame.transform.scale(house, (100, 50)))
    return houses
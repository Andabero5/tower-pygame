from abc import ABC,abstractmethod

class Floor(ABC):
    @abstractmethod
    def getFloor (self):
        pass

class YellowFloor(Floor):
    
    def getFloor(self):
        route = "Imagenes\Interfaz\Edificios\EdificioAmarillo.png"
        return route

class BlueFloor(Floor):

    def getFloor(self):
        route = "Imagenes\Interfaz\Edificios\EdificioAzul.jpg"
        return route

class FloorFactory():
      
    def getFloor(self,score):
        if score == 10:
            return YellowFloor.getFloor(self)
        elif score == 20:
            return BlueFloor.getFloor(self)
        

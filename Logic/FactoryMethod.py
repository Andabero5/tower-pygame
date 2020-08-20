from abc import ABC,abstractmethod

class Floor(ABC):
    @abstractmethod
    def getFloor (self):
        pass

class YellowFloor(Floor):
    
    def getFloor(self):
        route = "Images/Interface/Towers/tower-01.png"
        return route

class BlueFloor(Floor):

    def getFloor(self):
        route = "Images/Interface/Towers/tower-03.png"
        return route

class FloorFactory():
      
    def getFloor(self,score):
        if score == 10:
            return YellowFloor.getFloor(self)
        elif score == 20:
            return BlueFloor.getFloor(self)
        

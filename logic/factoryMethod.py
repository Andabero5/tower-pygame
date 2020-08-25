from abc import ABC, abstractmethod


class Floor(ABC):
    @abstractmethod
    def getFloor(self):
        pass


class YellowFloor(Floor):

    def getFloor(self):
        return "images\Interface\Towers//tower-01.png"


class RedFloor(Floor):

    def getFloor(self):
        return "images\Interface\Towers//tower-02.png"

class BlueFloor(Floor):

    def getFloor(self):
        return "images\Interface\Towers//tower-03.png"

class GreenFloor(Floor):

    def getFloor(self):
        return "images\Interface\Towers//tower-04.png"


class FloorFactory():
    @classmethod
    def getFloor(cls, option):
        if option == 1:
            return YellowFloor.getFloor(cls)
        elif option == 2:
            return RedFloor.getFloor(cls)
        elif option == 3:
            return BlueFloor.getFloor(cls)
        elif option==4:
            return GreenFloor.getFloor(cls)



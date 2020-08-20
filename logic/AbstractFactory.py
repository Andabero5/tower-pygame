from abc import ABC, abstractmethod


class Floor(ABC):
    @abstractmethod
    def getFloor(self):
        pass


class YellowFloor(Floor):

    def getFloor(self):
        route = "images\YellowFloor.png"
        return route


class BlueFloor(Floor):

    def getFloor(self):
        route = "images\BlueFloor.png"
        return route


class FloorFactory():
    @classmethod
    def getFloor(cls, score):
        if score == 10:
            return YellowFloor.getFloor(cls)
        elif score == 20:
            return BlueFloor.getFloor(cls)

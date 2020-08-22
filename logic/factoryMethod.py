from abc import ABC, abstractmethod


class Floor(ABC):
    @abstractmethod
    def getFloor(self):
        pass


class YellowFloor(Floor):

    def getFloor(self):
        return "images\YellowFloor.png"


class BlueFloor(Floor):

    def getFloor(self):
        return "images\BlueFloor.png"


class FloorFactory():
    @classmethod
    def getFloor(cls, score):
        if score == 10:
            return YellowFloor.getFloor(cls)
        elif score == 20:
            return BlueFloor.getFloor(cls)
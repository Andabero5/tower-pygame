from abc import ABC, abstractmethod
from random import choice


class Floor(ABC):
    @abstractmethod
    def getFloor(self):
        pass


class YellowFloor(Floor):

    def getFloor(self):
        return ["images\Interface\Towers//tower-01.png", [choice([5, -5]), 0]]


class RedFloor(Floor):

    def getFloor(self):
        return ["images\Interface\Towers//tower-02.png", [choice([7, -7]), 0]]


class BlueFloor(Floor):

    def getFloor(self):
        return ["images\Interface\Towers//tower-03.png", [choice([9, -9]), 0]]


class GreenFloor(Floor):

    def getFloor(self):
        return ["images\Interface\Towers//tower-04.png", [choice([9, -9]), 0]]


class FloorFactory():
    @classmethod
    def getFloor(cls, option):
        if option == 1:
            return YellowFloor.getFloor(cls)
        elif option == 2:
            return RedFloor.getFloor(cls)
        elif option == 3:
            return BlueFloor.getFloor(cls)
        elif option == 4:
            return GreenFloor.getFloor(cls)

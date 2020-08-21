from floor import Floor
from copy import copy, deepcopy


class Director():
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getFloor(self):
        floor = apartment()
        floor.setImage(self.__builder.buildImage())
        floor.setX(self.__builder.buildX())
        floor.setY(self.__builder.buildY())
        floor.setSpeed(self.__builder.buildSpeed())
        return floor

    def copy(self, image, x, y, speed):
        floor = Floor(image, x, y, speed)
        return copy(floor)


class Builder():
    def buildImage(self): pass
    def buildX(self): pass
    def buildY(self): pass
    def buildSpeed(self): pass


class YellowFloor(Builder):
    def buildImage(self):
        super().buildImage()
        return 'images\YellowFloor.png'

    def buildX(self):
        super().buildX()
        return 250

    def buildY(self):
        super().buildY()
        return 70

    def buildSpeed(self):
        super().buildSpeed()
        return [5, 0]


class BlueFloor(Builder):
    def buildImage(self):
        super().buildImage()
        return 'images\BlueFloor.png'

    def buildX(self):
        super().buildX()
        return 250

    def buildY(self):
        super().buildY()
        return 70

    def buildSpeed(self):
        super().buildSpeed()
        return [5, 0]


class apartment():
    def __init__(self):
        self.__image = ''
        self.__x = 0
        self.__y = 0
        self.__speed = []

    def setImage(self, image):
        self.__image = image

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def setSpeed(self, speed):
        self.__speed = speed

    def getImage(self):
        return self.__image

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getSpeed(self):
        return self.__speed


def main():
    yellowFloor = YellowFloor()
    director = Director()
    director.setBuilder(yellowFloor)
    data = director.getFloor()
    floor = director.copy(
        data.getImage(), data.getX(), data.getY(), data.getSpeed())
    print(floor)


if __name__ == "__main__":
    main()

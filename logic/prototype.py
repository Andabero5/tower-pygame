#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .floor import Floor
from .factoryMethod import FloorFactory


class FloorCreator():
    def __init__(self):
        self.__yellowFloor__ = Floor(FloorFactory.getFloor(1))
        self.__redFloor__ = Floor(FloorFactory.getFloor(2))
        self.__blueFloor__ = Floor(FloorFactory.getFloor(3))
        self.__greenFloor__ = Floor(FloorFactory.getFloor(4))

    def retrieveFloor(self, kindOfFloor):
        if "yellowFloor" == kindOfFloor:
            return self.__yellowFloor__.clone()
        if "redFloor" == kindOfFloor:
            return self.__redFloor__.clone()
        elif "blueFloor" == kindOfFloor:
            return self.__blueFloor__.clone()
        elif "greenFloor" == kindOfFloor:
            return self.__greenFloor__.clone()
        return None


class Prototype():
    def floorClone(self, colorFloor):
        creator = FloorCreator()
        floor = creator.retrieveFloor(colorFloor)
        return floor

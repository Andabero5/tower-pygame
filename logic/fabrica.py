#!/usr/bin/env python
# -*- coding: utf-8 -*-
from floor import Floor
from factoryMethod import FloorFactory


class FloorCreator():
    def __init__(self):
        self.__yellowFloor__ = Floor(FloorFactory.getFloor(10))
        self.__blueFloor__ = Floor(FloorFactory.getFloor(20))

    def retrieveFloor(self, kindOfFloor):
        if "yellowFloor" == kindOfFloor:
            return self.__yellowFloor__.clone()
        elif "blueFloor" == kindOfFloor:
            return self.__blueFloor__.clone()
        return None


class Prototype():
    def floorClone(self):
        creator = FloorCreator()
        floor = creator.retrieveFloor('blueFloor')
        return floor

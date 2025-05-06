"""Abstract class for a door & specfic class for a WoodenDoor"""

from abc import ABCMeta
from abc import abstractmethod


class Door(metaclass=ABCMeta):
    """Abstract class for a door"""

    def __subclasshook__(self, subclass):
        return(hasattr(subclass, 'get_width') and
               callable(subclass.get_width) and
               hasattr(subclass, 'get_height') and
               callable(subclass.get_height) or
               NotImplemented)

    @abstractmethod
    def get_width(self):
        """Get width of a door"""
        raise NotImplementedError

    @abstractmethod
    def get_height(self):
        """Get height of a door"""
        raise NotImplementedError


class WoodenDoor(Door):
    """A specific kind of door"""

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_width(self):
        """Get width of a door"""
        return self._width

    def get_height(self):
        """Get height of a door"""
        return self._height

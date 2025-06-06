"""Factory to make a door"""

from examples.designpatterns.simplefactory.door import Door
from examples.designpatterns.simplefactory.door import WoodenDoor


# pylint: disable=too-few-public-methods
class DoorFactory:
    """Factory to make a door"""

    @staticmethod
    def make_door(width, height) -> Door:
        """Make a door"""
        return WoodenDoor(width, height)

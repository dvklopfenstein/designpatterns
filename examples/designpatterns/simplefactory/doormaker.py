"""Make doors using factory"""

from examples.designpatterns.simplefactory.doorfactory import DoorFactory


def main():
    """Make different doors"""
    # Make me a door of 100x200
    door = DoorFactory.make_door(100, 200)
    print(f'Width:  {door.get_width()}')
    print(f'Height: {door.get_height()}\n')

    # Make me a door of 50x100
    door2 = DoorFactory.make_door(50, 100)
    print(f'Width:  {door2.get_width()}')
    print(f'Height: {door2.get_height()}\n')


if __name__ == '__main__':
    main()

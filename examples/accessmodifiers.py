"""Examples for Python access modifyers"""
# https://www.geeksforgeeks.org/access-modifiers-in-python-public-private-and-protected/

# program to illustrate protected access modifier in a class

# pylint: disable=too-few-public-methods
class Student:
    """super class"""

    # protected data members
    _name = None
    _roll = None
    _branch = None

    # constructor
    def __init__(self, name, roll, branch):
        self._name = name
        self._roll = roll
        self._branch = branch

    # protected member function
    def _display_roll_and_branch(self):

        # accessing protected data members
        print("Roll:", self._roll)
        print("Branch:", self._branch)

class Geek(Student):
    """derived class"""

    # constructor
    def __init__(self, name, roll, branch):
        Student.__init__(self, name, roll, branch)

    def display_details(self):
        """public member function"""

              # accessing protected data members of super class
        print("Name:", self._name)

        # accessing protected member functions of super class
        self._display_roll_and_branch()


def main():
    """Run example"""
    stu = Student("Alpha", 1234567, "Computer Science")
    print(dir(stu))

    # protected members and methods can be still accessed w pylint warning
    # pylint: disabple protected-access
    print(stu._name)
    stu._display_roll_and_branch()

    # Throws error
    # print(stu.name)
    # stu.displayRollAndBranch()

    # creating objects of the derived class
    obj = Geek("R2J", 1706256, "Information Technology")
    print("")
    print(dir(obj))

    # calling public member functions of the class
    obj.display_details()


if __name__ == '__main__':
    main()

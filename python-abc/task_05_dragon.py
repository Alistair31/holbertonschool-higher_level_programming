#!/usr/bin/python3
"""

"""


class SwimMixin:
    """
    Docstring for SwimMixin
    """

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    Docstring for FlyMixin
    """

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Docstring for FlyingFish
    """

    def swim(self):
        print("The flying fish is swimming!")

    def fly(self):
        print("The flying fish is soaring!")

    def roar(self):
        print("The dragon roars!")

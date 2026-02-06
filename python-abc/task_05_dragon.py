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

    def roar(self):
        print("The dragon roars!")

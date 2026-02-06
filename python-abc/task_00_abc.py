#!/usr/bin/python3
from abc import ABC, abstractmethod
"""
Define an abstract class, abstract method and and use them in subclass
"""


class Animal(ABC):
    """
    Define a class of animal
    """

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    Class Dog
    """

    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    Class Cat
    """

    def sound(self):
        return "Meow"

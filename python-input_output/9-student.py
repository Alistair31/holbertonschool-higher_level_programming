#!/usr/bin/python3
"""
python-input_output.9-student
"""


class Student:
    """
    Student
    """

    def __init__(self, first_name, last_name, age):
        """
        __init__

        :param self: Recall of itself
        :param first_name: First name of the student
        :param last_name: Last name of the student
        :param age: Age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        to_json

        :param self: recall of itself
        """
        return self.__dict__

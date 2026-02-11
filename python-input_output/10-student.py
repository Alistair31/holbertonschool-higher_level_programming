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

    def to_json(self, attrs=None):
        """
        to_json

        :param self: recall of itself
        """
        if isinstance(attrs, list) is False:
            return self.__dict__

        for item in attrs:
            if isinstance(item, str) is False:
                return self.__dict__
        fattrs = {}
        for key in attrs:
            if isinstance(key, str) and key in self.__dict__:
                fattrs[key] = self.__dict__[key]
        return fattrs

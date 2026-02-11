#!/usr/bin/python3
import pickle
"""
python-serialization.task_01_pickle
"""


class CustomObject:
    """
    CustomObject
    """

    def __init__(self, name, age, is_student):
        """
        __init__

        :param self: Recall of class
        :param name: Name
        :param age: Age
        :param is_student: Status
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display

        :param self: Recall of class
        """
        print(f"Name: {str(self.name)}")
        print(f"Age: {int(self.age)}")
        print(f"Is Student: {bool(self.is_student)}")

    def serialize(self, filename):
        """
        Serialize

        :param self: Recall of class
        :param filename: Name of the filename
        """
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize

        :param cls: Recall
        :param filename: Name of the file
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None

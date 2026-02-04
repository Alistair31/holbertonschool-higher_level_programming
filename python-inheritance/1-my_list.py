#!/usr/bin/python3
"""
Python-inheritance.1-my_list
"""


class MyList(list):
    """
    Class that define a list
    """

    def print_sorted(self):
        """
        Method of print a sorted list

        :param self: Recall itself (MyList)
        """

        print(sorted(self))

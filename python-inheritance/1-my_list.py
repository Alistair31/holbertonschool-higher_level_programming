#!/usr/bin/python3
"""
Python-inheritance.1-my_list
"""


class MyList(list):
    """
    Docstring for Mylist
    """

    def print_sorted(self):
        """
        Method ofr print a sorted list

        :param self: Recall itself (MyList)
        """

        print(sorted(self))

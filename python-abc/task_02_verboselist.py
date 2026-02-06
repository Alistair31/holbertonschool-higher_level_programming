#!/usr/bin/python3
"""

"""


class VerboseList(list):
    """
    Docstring for VerboseList
    """

    def append(self, item):
        print(f"Added {item} to the list.")
        super().append(item)

    def extend(self, item):
        print(f"Extend the list with {item} items.")
        super().extend(item)

    def remove(self, item):
        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=-1):
        print(f"Popped {self[index]} from the list.")
        super().pop(index)

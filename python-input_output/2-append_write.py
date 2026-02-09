#!/usr/bin/python3
"""
Python-input_output.2-append_write
"""


def append_write(filename="", text=""):
    """
    append_write

    :param filename: Name of the file to append on / create
    :param text: Text to append on file
    """
    with open(filename, "a") as f:
        return f.write(text)

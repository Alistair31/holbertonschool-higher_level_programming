#!/usr/bin/python3
"""
Python-input_output.1-write_file
"""


def write_file(filename="", text=""):
    """
    write_file

    :param filename: Name of the file to write on / create
    :param text: Text to write on file
    """
    with open(filename, "w") as f:
        return f.write(text)

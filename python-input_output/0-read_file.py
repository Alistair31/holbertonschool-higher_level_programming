#!/usr/bin/python3
"""
python-input_output.0-read_file
"""


def read_file(filename=""):
    """
    read_file

    :param filename: File to read
    """
    with open(filename, "r") as f:
        print(f.read())

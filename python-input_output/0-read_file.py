#!/usr/bin/python3
"""
python-input_output.0-read_file
"""


def read_file(filename=""):
    with open(filename, "r") as f:
        print(f.read())
        f.close()

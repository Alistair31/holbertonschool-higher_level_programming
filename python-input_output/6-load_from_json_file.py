#!/usr/bin/python3
"""
python-input_output.6-load_from_json_file
"""


def load_from_json_file(filename):
    """
    load_from_json_file

    :param filename: Name of the file to load from
    """
    import json
    with open(filename, "r") as f:
        return json.load(f)

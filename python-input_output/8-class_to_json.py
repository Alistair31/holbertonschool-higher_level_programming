#!/usr/bin/python3
"""
python-input_output.8-class_to_json
"""


def class_to_json(obj):
    """
    class_to_json

    :param obj: Object to return all the attribute of
    """
    return obj.__dict__

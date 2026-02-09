#!/usr/bin/python3
import json
"""
python-input_output.4-from_json_string
"""


def from_json_string(my_str):
    """
    from_json_string

    :param my_str: string to turn into object
    """
    return json.loads(my_str)

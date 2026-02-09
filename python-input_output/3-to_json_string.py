#!/usr/bin/python3
import json
"""
python-input_output.3-to_json_string
"""


def to_json_string(my_obj):
    """
    to_json_string

    :param my_obj: object to serialize
    """
    return json.dumps(my_obj)

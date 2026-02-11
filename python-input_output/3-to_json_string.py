#!/usr/bin/python3
"""
python-input_output.3-to_json_string
"""


def to_json_string(my_obj):
    """
    to_json_string

    :param my_obj: object to serialize
    """
    import json
    return json.dumps(my_obj)

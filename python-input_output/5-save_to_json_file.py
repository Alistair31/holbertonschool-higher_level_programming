#!/usr/bin/python3
"""
python-input_output.5-save_to_json_file
"""


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file

    :param my_obj: Object
    :param filename: Description
    """
    import json
    with open(filename, "w") as f:
        j = json.dumps(my_obj)
        return f.write(j)

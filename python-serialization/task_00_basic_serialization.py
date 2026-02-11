#!/usr/bin/python3
import json
import pickle
"""
python-serialization.task_00_basic_serialization
"""


def serialize_and_save_to_file(data, filename):
    """
    serialize_and_save_to_file

    :param data: Data to save
    :param filename: File
    """
    with open(filename, "w") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    load_and_deserialize

    :param filename: File to load
    """
    with open(filename, "r") as f:
        return json.load(f)
